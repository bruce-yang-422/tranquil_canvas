import argparse
import base64
import os
import sys
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# 常用尺寸參考：
#   1024x1024  — 正方形，生成最快
#   1536x1024  — 橫式 (3:2)
#   1024x1536  — 直式 (2:3)
#   2048x1152  — 16:9 橫式，最接近 16:9 的常用尺寸
#   1152x2048  — 9:16 直式，最接近 9:16 的常用尺寸（海報、手機桌布）
#   2048x2048  — 2K 正方形 (experimental)
#   3840x2160  — 4K 橫式 (experimental)
#   2160x3840  — 4K 直式 (experimental，最大解析度)
#   最大邊 3840px，比例不超過 3:1，須為 16px 的倍數
SIZES = [
    "1024x1024",
    "1536x1024",
    "1024x1536",
    "2048x2048",
    "2048x1152",
    "1152x2048",
    "3840x2160",
    "2160x3840",
]
QUALITIES = ["low", "medium", "high", "auto"]
DEFAULT_INPUT_DIR = Path("input")
DEFAULT_OUTPUT_DIR = Path("output")
DEFAULT_PROMPT_FILE = DEFAULT_INPUT_DIR / "prompt.txt"


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
    if prompt_path.suffix.lower() != ".txt":
        raise ValueError(f"prompt 檔案必須是 .txt：{prompt_path}")

    prompt = prompt_path.read_text(encoding="utf-8").strip()
    if not prompt:
        raise ValueError(f"prompt 檔案是空的：{prompt_path}")
    return prompt


def resolve_output_path(output_name: str, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = Path(output_name)

    if output_path.is_absolute():
        output_path.parent.mkdir(parents=True, exist_ok=True)
        return output_path

    return output_dir / output_path


def generate_image(
    prompt: str,
    output_path: Path,
    size: str = "1024x1024",
    quality: Literal["low", "medium", "high", "auto"] = "medium",
) -> Path:
    client = OpenAI()

    print("[*] 正在送出 prompt，等待 gpt-image-2 回應...")
    print(f"    尺寸   : {size}  畫質: {quality}")

    result = client.images.generate(
        model="gpt-image-2",
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


if __name__ == "__main__":
    if not os.environ.get("OPENAI_API_KEY"):
        print("[-] 錯誤：找不到 OPENAI_API_KEY，請在 .env 或系統環境變數中設定。")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="gpt-image-2 終端機產圖工具")
    parser.add_argument(
        "-p",
        "--prompt-file",
        default=str(DEFAULT_PROMPT_FILE),
        help="prompt 文字檔路徑（預設: input/prompt.txt）",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="output.png",
        help="輸出檔名（預設會存到 output/ 內）",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="輸出資料夾（預設: output）",
    )
    parser.add_argument("-s", "--size", default="1024x1024", choices=SIZES, help="圖片尺寸")
    parser.add_argument("-q", "--quality", default="medium", choices=QUALITIES, help="畫質")
    args = parser.parse_args()

    prompt_path = resolve_prompt_path(args.prompt_file, DEFAULT_INPUT_DIR)
    output_dir = Path(args.output_dir)

    try:
        prompt = load_prompt(prompt_path)
        output_path = resolve_output_path(args.output, output_dir)
    except (FileNotFoundError, ValueError) as exc:
        print(f"[-] 錯誤：{exc}")
        sys.exit(1)

    generate_image(prompt, output_path, args.size, args.quality)
