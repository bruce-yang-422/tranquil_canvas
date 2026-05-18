"""
把 input/*.md（# style + # image 結構）
轉換成 input/*_by-hand.md（每個 image 內嵌完整 style）
"""

import sys
from pathlib import Path

from main import parse_markdown_batch

INPUT_DIR = Path("input")


def pick_md_files() -> list[Path]:
    md_files = sorted(
        f for f in INPUT_DIR.glob("*.md") if not f.stem.endswith("_by-hand")
    )
    if not md_files:
        print(f"[-] {INPUT_DIR}/ 底下沒有可轉換的 .md 檔案")
        sys.exit(1)

    print("\n可用的檔案：")
    for i, f in enumerate(md_files, 1):
        print(f"  {i}. {f.name}")
    print(f"  0. all（全部轉換）")

    while True:
        raw = input(f"\n請選擇 [0-{len(md_files)}]：").strip()
        if raw == "0":
            return md_files
        if raw.isdigit() and 1 <= int(raw) <= len(md_files):
            return [md_files[int(raw) - 1]]
        print("  輸入無效，請重試")


def convert(src: Path) -> Path:
    style_prompt, items = parse_markdown_batch(src)
    dst = src.with_name(src.stem + "_by-hand.md")

    lines: list[str] = []
    for name, scene_prompt in items:
        lines.append(f"# {name}")
        lines.append("```")
        if style_prompt:
            lines.append(style_prompt)
            lines.append("")
        lines.append(scene_prompt)
        lines.append("```")
        lines.append("")

    dst.write_text("\n".join(lines), encoding="utf-8")
    print(f"[+] {src.name}  →  {dst.name}")
    return dst


def main() -> None:
    print("=== by-hand 格式轉換工具 ===")
    selected = pick_md_files()
    for src in selected:
        convert(src)
    print("\n完成。")


if __name__ == "__main__":
    main()
