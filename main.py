import argparse
import base64
import mimetypes
import os
import sys
from contextlib import ExitStack
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# 常用尺寸參考：
#   1024x1024  — 正方形，生成最快
#   1440x1440  — 中等解析度正方形
#   1536x1088  — 長邊 1536 的 A2 橫式（適合 medium / high）
#   1088x1536  — 長邊 1536 的 A2 直式（適合 medium / high）
#   2048x1440  — 長邊 2048 的 A2 橫式（高解析）
#   1440x2048  — 長邊 2048 的 A2 直式（高解析）
#   3840x2720  — 長邊 3840 的 A2 橫式（實驗性超高解析）
#   2720x3840  — 長邊 3840 的 A2 直式（實驗性超高解析）
#   1536x1024  — 橫式 (3:2)
#   1024x1536  — 直式 (2:3)
#   2048x1152  — 16:9 橫式，最接近 16:9 的常用尺寸
#   1152x2048  — 9:16 直式，最接近 9:16 的常用尺寸（海報、手機桌布）
#   2048x880   — 21:9 橫式超寬螢幕（電影感）
#   880x2048   — 9:21 直式超高（實驗性）
#   3840x1648  — 21:9 橫式超寬 4K（實驗性）
#   1648x3840  — 9:21 直式超高 4K（實驗性）
#   2048x2048  — 2K 正方形 (experimental)
#   3840x2160  — 4K 橫式 (experimental)
#   2160x3840  — 4K 直式 (experimental，最大解析度)
#   最大邊 3840px，比例不超過 3:1，須為 16px 的倍數
SIZES = [
    "1024x1024",
    "1440x1440",
    "1536x1088",
    "1088x1536",
    "2048x1440",
    "1440x2048",
    "1536x1024",
    "1024x1536",
    "2048x2048",
    "2048x1152",
    "1152x2048",
    "2048x880",
    "880x2048",
    "3840x2720",
    "2720x3840",
    "3840x2160",
    "2160x3840",
    "3840x1648",
    "1648x3840",
]
SIZE_CHOICES = ["auto", *SIZES]
QUALITIES = ["low", "medium", "high", "auto"]
IMAGE_MODES = ["generate", "style-reference", "edit", "chatgpt-reference"]
FIDELITY_CHOICES = ["low", "high"]
DEFAULT_INPUT_DIR = Path("input")
DEFAULT_OUTPUT_DIR = Path("output")
DEFAULT_PROMPT_FILE = DEFAULT_INPUT_DIR / "prompt.txt"
DEFAULT_BATCH_PREFIX = "image"
TEXT_PROMPT_EXTENSIONS = {".txt", ".md"}
IMAGE_FILE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
GENERATE_MODEL = "gpt-image-2"
EDIT_MODEL = "gpt-image-1"
STYLE_ANALYSIS_MODEL = "gpt-4.1-mini"
CHATGPT_REFERENCE_MODEL = "gpt-5.5"


def resolve_prompt_path(prompt_name: str, input_dir: Path) -> Path:
    prompt_path = Path(prompt_name)

    if prompt_path.is_absolute():
        return prompt_path

    if prompt_path.parent != Path("."):
        return prompt_path

    return input_dir / prompt_path


def load_prompt(prompt_path: Path) -> str:
    if not prompt_path.exists():
        raise FileNotFoundError(f"找不到 prompt 檔案：{prompt_path}")
    if prompt_path.suffix.lower() not in TEXT_PROMPT_EXTENSIONS:
        raise ValueError(f"prompt 檔案必須是 .txt 或 .md：{prompt_path}")

    prompt = prompt_path.read_text(encoding="utf-8").strip()
    if not prompt:
        raise ValueError(f"prompt 檔案是空的：{prompt_path}")
    return prompt


def resolve_input_asset_path(asset_name: str, input_dir: Path) -> Path:
    asset_path = Path(asset_name)

    if asset_path.is_absolute():
        return asset_path

    if asset_path.exists():
        return asset_path

    return input_dir / asset_path


def resolve_image_paths(image_args: list[str] | None, input_dir: Path) -> list[Path]:
    if not image_args:
        return []

    resolved_paths: list[Path] = []
    for raw_path in image_args:
        path = resolve_input_asset_path(raw_path, input_dir)
        if not path.exists():
            raise FileNotFoundError(f"找不到參考圖片：{path}")
        if path.suffix.lower() not in IMAGE_FILE_EXTENSIONS:
            allowed = ", ".join(sorted(IMAGE_FILE_EXTENSIONS))
            raise ValueError(f"參考圖片格式不支援：{path}（僅支援 {allowed}）")
        resolved_paths.append(path)

    if len(resolved_paths) > 16:
        raise ValueError("參考圖片最多只能提供 16 張")

    return resolved_paths


def parse_markdown_batch(batch_path: Path) -> tuple[str | None, list[tuple[str | None, str]]]:
    raw_text = load_prompt(batch_path)
    current_section: str | None = None
    current_lines: list[str] = []
    style_prompt: str | None = None
    items: list[tuple[str | None, str]] = []

    def normalize_section_content(content: str) -> str:
        stripped = content.strip()
        lines = stripped.splitlines()
        if len(lines) >= 2 and lines[0].strip().startswith("```") and lines[-1].strip() == "```":
            return "\n".join(lines[1:-1]).strip()
        return stripped

    def flush_section() -> None:
        nonlocal current_section, current_lines, style_prompt, items
        if current_section is None:
            current_lines = []
            return

        content = normalize_section_content("\n".join(current_lines))
        if not content:
            current_lines = []
            return

        section_name = current_section.strip()
        section_key = section_name.lower()
        if section_key == "style":
            style_prompt = content
        elif section_key.startswith("image"):
            items.append((section_name, content))
        else:
            raise ValueError(f"不支援的 Markdown 區塊標題：{section_name}")

        current_lines = []

    for raw_line in raw_text.splitlines():
        stripped = raw_line.strip()
        if stripped.startswith("#"):
            flush_section()
            current_section = stripped.lstrip("#").strip()
            continue

        if current_section is not None:
            current_lines.append(raw_line)

    flush_section()

    if not items:
        raise ValueError(f"Markdown 批次檔沒有任何 `# image ...` 區塊：{batch_path}")

    return style_prompt, items


def load_batch_items(batch_path: Path) -> list[tuple[str | None, str]]:
    raw_text = load_prompt(batch_path)
    items: list[tuple[str | None, str]] = []

    for line_number, raw_line in enumerate(raw_text.splitlines(), start=1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        if "|" in line:
            name_part, prompt_part = line.split("|", 1)
            name = name_part.strip() or None
            prompt = prompt_part.strip()
        else:
            name = None
            prompt = line

        if not prompt:
            raise ValueError(f"批次檔第 {line_number} 行沒有 prompt：{batch_path}")

        items.append((name, prompt))

    if not items:
        raise ValueError(f"批次檔沒有可用內容：{batch_path}")

    return items


def build_combined_prompt(style_prompt: str | None, scene_prompt: str) -> str:
    if not style_prompt:
        return scene_prompt
    return f"{style_prompt.strip()}\n\n{scene_prompt.strip()}"


def load_batch_definition(batch_path: Path) -> tuple[str | None, list[tuple[str | None, str]]]:
    if batch_path.suffix.lower() == ".md":
        return parse_markdown_batch(batch_path)
    return None, load_batch_items(batch_path)


def parse_image_range(range_text: str, total_items: int) -> tuple[int, int]:
    if "-" not in range_text:
        raise ValueError("--range 格式必須是 起始-結束，例如 2-5")

    start_text, end_text = range_text.split("-", 1)
    try:
        start = int(start_text.strip())
        end = int(end_text.strip())
    except ValueError as exc:
        raise ValueError("--range 必須是數字範圍，例如 2-5") from exc

    if start < 1 or end < 1 or start > total_items or end > total_items:
        raise ValueError(f"--range 必須介於 1 到 {total_items} 之間")
    if start > end:
        raise ValueError("--range 的起始值不能大於結束值")

    return start, end


def parse_skip_images(skip_text: str, total_items: int) -> set[int]:
    skipped: set[int] = set()
    for raw_part in skip_text.split(","):
        part = raw_part.strip()
        if not part:
            continue
        try:
            image_index = int(part)
        except ValueError as exc:
            raise ValueError("--skip-images 必須是逗號分隔的數字，例如 3,5,7") from exc

        if image_index < 1 or image_index > total_items:
            raise ValueError(f"--skip-images 必須介於 1 到 {total_items} 之間")
        skipped.add(image_index)

    return skipped


def parse_images_list(images_text: str, total_items: int) -> list[int]:
    indices: list[int] = []
    for raw_part in images_text.split(","):
        part = raw_part.strip()
        if not part:
            continue
        try:
            image_index = int(part)
        except ValueError as exc:
            raise ValueError("--images 必須是逗號分隔的數字，例如 8,11,13") from exc

        if image_index < 1 or image_index > total_items:
            raise ValueError(f"--images 必須介於 1 到 {total_items} 之間")
        indices.append(image_index)

    return indices


def select_batch_items(
    batch_items: list[tuple[str | None, str]],
    selected_image: int | None,
    from_image: int | None,
    range_text: str | None,
    skip_images_text: str | None,
    images_list_text: str | None = None,
) -> list[tuple[str | None, str]]:
    total_items = len(batch_items)

    if images_list_text is not None:
        indices = parse_images_list(images_list_text, total_items)
        selected = [batch_items[i - 1] for i in indices]
    elif selected_image is not None:
        if selected_image < 1 or selected_image > total_items:
            raise ValueError(f"--image 必須介於 1 到 {total_items} 之間")
        selected = [batch_items[selected_image - 1]]
    elif range_text is not None:
        start, end = parse_image_range(range_text, total_items)
        selected = [
            item
            for index, item in enumerate(batch_items, start=1)
            if start <= index <= end
        ]
    elif from_image is not None:
        if from_image < 1 or from_image > total_items:
            raise ValueError(f"--from-image 必須介於 1 到 {total_items} 之間")
        selected = [
            item
            for index, item in enumerate(batch_items, start=1)
            if index >= from_image
        ]
    else:
        selected = list(batch_items)

    if skip_images_text and images_list_text is None:
        skipped = parse_skip_images(skip_images_text, total_items)
        selected = [
            item
            for index, item in enumerate(batch_items, start=1)
            if item in selected and index not in skipped
        ]

    if not selected:
        raise ValueError("篩選後沒有任何要輸出的圖片，請檢查 --image / --images / --from-image / --range / --skip-images")

    return selected


def resolve_output_path(output_name: str, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = Path(output_name)

    if output_path.is_absolute():
        output_path.parent.mkdir(parents=True, exist_ok=True)
        return output_path

    return output_dir / output_path


def sanitize_output_stem(name: str) -> str:
    allowed = []
    for char in name.strip():
        if char.isalnum() or char in {"-", "_"}:
            allowed.append(char)
        elif char in {" ", "."}:
            allowed.append("_")
    stem = "".join(allowed).strip("_")
    return stem or DEFAULT_BATCH_PREFIX


def build_style_reference_prompt(prompt: str) -> str:
    return (
        "請根據下列風格描述來生成新圖。"
        "只借用配色、質感、版式語氣、插畫筆觸或設計語言，"
        "不要直接複製原圖的主體、構圖、文字、logo 或可辨識內容。"
        "\n\n"
        f"{prompt.strip()}"
    )


def build_edit_prompt(prompt: str) -> str:
    return (
        "請以輸入圖片為基礎進行重繪或改圖，"
        "保留原圖的核心主體、主要構圖與關鍵資訊，"
        "再依照下列需求修改、增補或重設風格。"
        "\n\n"
        f"{prompt.strip()}"
    )


def image_path_to_data_url(image_path: Path) -> str:
    mime_type, _ = mimetypes.guess_type(image_path.name)
    if not mime_type:
        mime_type = "image/png"
    image_b64 = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{image_b64}"


def summarize_reference_style(client: OpenAI, image_paths: list[Path]) -> str:
    if not image_paths:
        raise ValueError("風格參考模式至少要提供一張圖片")

    content: list[dict[str, str]] = [
        {
            "type": "input_text",
            "text": (
                "請分析這些參考圖片共同的視覺風格，只描述風格，不要描述特定主體內容。"
                "請輸出一段精簡但可直接拿去生成圖片的中文風格摘要。"
                "重點包含：配色、明暗、材質、插畫或攝影風格、構圖習慣、資訊密度、字體氣質、整體情緒。"
                "避免提到具體人物、物件、地名、品牌、logo、畫面文字。"
                "只輸出摘要本身，不要加標題、清單符號或前言。"
            ),
        }
    ]

    for image_path in image_paths:
        content.append(
            {
                "type": "input_image",
                "image_url": image_path_to_data_url(image_path),
            }
        )

    response = client.responses.create(
        model=STYLE_ANALYSIS_MODEL,
        input=[{"role": "user", "content": content}],
        max_output_tokens=400,
    )
    style_summary = response.output_text.strip()
    if not style_summary:
        raise ValueError("無法從參考圖提取風格摘要")

    return style_summary


def extract_image_b64_from_response(response) -> str:
    for item in getattr(response, "output", []) or []:
        if getattr(item, "type", None) == "image_generation_call":
            result = getattr(item, "result", None)
            if result:
                return result

    response_dict = response.model_dump() if hasattr(response, "model_dump") else {}
    for item in response_dict.get("output", []):
        if item.get("type") == "image_generation_call" and item.get("result"):
            return item["result"]

    raise ValueError("Responses API 未回傳圖片資料")


def generate_image_with_chatgpt_reference(
    client: OpenAI,
    prompt: str,
    image_paths: list[Path],
    output_path: Path,
    size: str = "1024x1024",
    quality: Literal["low", "medium", "high", "auto"] = "medium",
) -> Path:
    if not image_paths:
        raise ValueError("chatgpt-reference 模式至少要提供一張圖片")

    print("[*] 正在用 ChatGPT 風格參考模式送出請求...")
    print(f"    尺寸   : {size}  畫質: {quality}  參考圖: {len(image_paths)} 張")

    content: list[dict[str, str]] = [
        {
            "type": "input_text",
            "text": (
                "請參考這些圖片的視覺風格、版面感、資訊密度、插畫語氣與排版傾向，"
                "但不要直接複製原圖主體、文字或構圖。"
                "\n\n"
                f"{prompt.strip()}"
            ),
        }
    ]
    for image_path in image_paths:
        content.append(
            {
                "type": "input_image",
                "image_url": image_path_to_data_url(image_path),
            }
        )

    response = client.responses.create(
        model=CHATGPT_REFERENCE_MODEL,
        input=[{"role": "user", "content": content}],
        tools=[
            {
                "type": "image_generation",
                "size": size,
                "quality": quality,
            }
        ],
    )

    image_b64 = extract_image_b64_from_response(response)
    image_bytes = base64.b64decode(image_b64)
    output_path.write_bytes(image_bytes)

    print(f"[+] 已儲存：{output_path.resolve()}")
    return output_path


def generate_image(
    client: OpenAI,
    prompt: str,
    output_path: Path,
    size: str = "1024x1024",
    quality: Literal["low", "medium", "high", "auto"] = "medium",
) -> Path:
    print("[*] 正在送出 prompt，等待 gpt-image-2 回應...")
    print(f"    尺寸   : {size}  畫質: {quality}")

    result = client.images.generate(
        model=GENERATE_MODEL,
        prompt=prompt,
        size=size,
        quality=quality,
    )

    image_b64 = result.data[0].b64_json
    assert image_b64, "API 未回傳圖片資料"
    image_bytes = base64.b64decode(image_b64)

    output_path.write_bytes(image_bytes)

    print(f"[+] 已儲存：{output_path.resolve()}")
    return output_path


def edit_image(
    client: OpenAI,
    prompt: str,
    image_paths: list[Path],
    output_path: Path,
    size: str = "1024x1024",
    quality: Literal["low", "medium", "high", "auto"] = "medium",
    input_fidelity: Literal["low", "high"] = "high",
) -> Path:
    if not image_paths:
        raise ValueError("圖片參考模式至少要提供一張圖片")

    print("[*] 正在送出圖片參考請求，等待模型回應...")
    print(f"    尺寸   : {size}  畫質: {quality}  參考圖: {len(image_paths)} 張  fidelity: {input_fidelity}")

    with ExitStack() as stack:
        images = [stack.enter_context(path.open("rb")) for path in image_paths]
        result = client.images.edit(
            model=EDIT_MODEL,
            image=images,
            prompt=prompt,
            size=size,
            quality=quality,
            input_fidelity=input_fidelity,
        )

    image_b64 = result.data[0].b64_json
    assert image_b64, "API 未回傳圖片資料"
    image_bytes = base64.b64decode(image_b64)

    output_path.write_bytes(image_bytes)

    print(f"[+] 已儲存：{output_path.resolve()}")
    return output_path


def generate_batch(
    client: OpenAI,
    batch_items: list[tuple[str | None, str]],
    output_dir: Path,
    size: str,
    quality: Literal["low", "medium", "high", "auto"],
    style_prompt: str | None,
    batch_prefix: str,
    image_mode: Literal["generate", "style-reference", "edit"],
    reference_images: list[Path],
    input_fidelity: Literal["low", "high"],
) -> list[Path]:
    results: list[Path] = []
    output_dir.mkdir(parents=True, exist_ok=True)

    for index, (custom_name, scene_prompt) in enumerate(batch_items, start=1):
        stem = sanitize_output_stem(custom_name or f"{batch_prefix}_{index:02d}")
        output_path = output_dir / f"{stem}.png"
        combined_prompt = build_combined_prompt(style_prompt, scene_prompt)

        print(f"[{index}/{len(batch_items)}] 生成中：{output_path.name}")
        if image_mode == "generate":
            result = generate_image(client, combined_prompt, output_path, size, quality)
        elif image_mode == "style-reference":
            style_summary = summarize_reference_style(client, reference_images)
            style_prompt = build_style_reference_prompt(
                f"[參考風格摘要]\n{style_summary}\n\n[本次需求]\n{combined_prompt}"
            )
            result = generate_image(client, style_prompt, output_path, size, quality)
        elif image_mode == "chatgpt-reference":
            result = generate_image_with_chatgpt_reference(
                client,
                combined_prompt,
                reference_images,
                output_path,
                size,
                quality,
            )
        else:
            result = edit_image(
                client,
                build_edit_prompt(combined_prompt),
                reference_images,
                output_path,
                size,
                quality,
                input_fidelity,
            )

        results.append(result)

    return results


if __name__ == "__main__":
    if not os.environ.get("OPENAI_API_KEY"):
        print("[-] 錯誤：找不到 OPENAI_API_KEY，請在 .env 或系統環境變數中設定。")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="gpt-image-2 終端機產圖工具")
    parser.add_argument(
        "-p",
        "--prompt-file",
        default=str(DEFAULT_PROMPT_FILE),
        help="單張模式的 prompt 文字檔路徑（預設: input/prompt.txt）",
    )
    parser.add_argument(
        "-b",
        "--batch-file",
        help="批次模式的 prompt 檔；可用 `.txt` 每行一張，或 `.md` 的 `# style` / `# image xx` 結構",
    )
    parser.add_argument(
        "--style-file",
        help="批次模式共用的風格 prompt 檔",
    )
    parser.add_argument(
        "--batch-prefix",
        default=DEFAULT_BATCH_PREFIX,
        help="批次模式未指定檔名時的預設前綴（預設: image）",
    )
    parser.add_argument(
        "--image-mode",
        default="generate",
        choices=IMAGE_MODES,
        help="圖片模式：generate=純文字生圖，style-reference=先萃取風格再生圖，chatgpt-reference=像 ChatGPT 一樣把圖當上下文生圖，edit=以參考圖重繪/改圖",
    )
    parser.add_argument(
        "--ref",
        action="append",
        dest="reference_images",
        help="參考圖片路徑；可重複指定多次。style-reference 與 edit 模式至少要提供一張",
    )
    parser.add_argument(
        "--input-fidelity",
        default="high",
        choices=FIDELITY_CHOICES,
        help="參考圖保真度（僅 style-reference / edit 模式有效）",
    )
    parser.add_argument(
        "--image",
        type=int,
        help="批次模式只輸出指定的第幾張（從 1 開始）",
    )
    parser.add_argument(
        "--from-image",
        type=int,
        help="批次模式從指定張數開始一路輸出到最後（從 1 開始）",
    )
    parser.add_argument(
        "--range",
        dest="image_range",
        help="批次模式只輸出指定範圍，例如 2-5",
    )
    parser.add_argument(
        "--images",
        help="批次模式只輸出指定的幾張，逗號分隔，例如 8,11,13",
    )
    parser.add_argument(
        "--skip-images",
        help="批次模式跳過指定張數，格式例如 3,7,9",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="output.png",
        help="單張模式輸出檔名（預設會存到 output/ 內）",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="輸出資料夾（預設: output）",
    )
    parser.add_argument(
        "-s",
        "--size",
        default="1024x1024",
        choices=SIZE_CHOICES,
        help="圖片尺寸；可用 auto 讓模型自動決定",
    )
    parser.add_argument("-q", "--quality", default="medium", choices=QUALITIES, help="畫質")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)

    try:
        client = OpenAI()
        reference_images = resolve_image_paths(args.reference_images, DEFAULT_INPUT_DIR)

        if args.image_mode != "generate" and not reference_images:
            raise ValueError("--image-mode 為 style-reference、chatgpt-reference 或 edit 時，至少要提供一張 --ref 圖片")
        if args.image_mode == "generate" and reference_images:
            print("[!] 提醒：目前是 generate 模式，已忽略 --ref 圖片。若要使用參考圖，請加上 --image-mode style-reference 或 --image-mode edit。")

        if args.batch_file:
            batch_path = resolve_prompt_path(args.batch_file, DEFAULT_INPUT_DIR)
            markdown_style_prompt, batch_items = load_batch_definition(batch_path)
            batch_items = select_batch_items(
                batch_items,
                args.image,
                args.from_image,
                args.image_range,
                args.skip_images,
                args.images,
            )
            style_prompt = markdown_style_prompt
            if args.style_file:
                style_path = resolve_prompt_path(args.style_file, DEFAULT_INPUT_DIR)
                extra_style_prompt = load_prompt(style_path)
                style_prompt = build_combined_prompt(extra_style_prompt, style_prompt) if style_prompt else extra_style_prompt

            generate_batch(
                client,
                batch_items,
                output_dir,
                args.size,
                args.quality,
                style_prompt,
                sanitize_output_stem(args.batch_prefix),
                args.image_mode,
                reference_images,
                args.input_fidelity,
            )
        else:
            prompt_path = resolve_prompt_path(args.prompt_file, DEFAULT_INPUT_DIR)
            prompt = load_prompt(prompt_path)
            output_path = resolve_output_path(args.output, output_dir)
            if args.image_mode == "generate":
                generate_image(client, prompt, output_path, args.size, args.quality)
            elif args.image_mode == "style-reference":
                style_summary = summarize_reference_style(client, reference_images)
                styled_prompt = build_style_reference_prompt(
                    f"[參考風格摘要]\n{style_summary}\n\n[本次需求]\n{prompt}"
                )
                generate_image(client, styled_prompt, output_path, args.size, args.quality)
            elif args.image_mode == "chatgpt-reference":
                generate_image_with_chatgpt_reference(
                    client,
                    prompt,
                    reference_images,
                    output_path,
                    args.size,
                    args.quality,
                )
            else:
                edit_image(
                    client,
                    build_edit_prompt(prompt),
                    reference_images,
                    output_path,
                    args.size,
                    args.quality,
                    args.input_fidelity,
                )
    except (FileNotFoundError, ValueError) as exc:
        print(f"[-] 錯誤：{exc}")
        sys.exit(1)
