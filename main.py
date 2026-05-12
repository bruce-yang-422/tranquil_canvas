import argparse
import base64
import os
import sys
from pathlib import Path
from typing import Literal
from dotenv import load_dotenv
from openai import OpenAI
from prompt import PROMPT

load_dotenv()

# 常用尺寸參考：
#   1024x1024  — 正方形，生成最快
#   1536x1024  — 橫式 (3:2)
#   1024x1536  — 直式 (2:3)
#   2048x2048  — 2K 正方形 (experimental)
#   2048x1152  — 2K 橫式 (experimental)
#   1152x2048  — 2K 直式 (experimental)
#   3840x2160  — 4K 橫式 (experimental)
#   2160x3840  — 4K 直式 (experimental，最大解析度)
#   最大邊 3840px，比例不超過 3:1，須為 16px 的倍數
SIZES = [
    "1024x1024", "1536x1024", "1024x1536",
    "2048x2048", "2048x1152", "1152x2048",
    "3840x2160", "2160x3840",
]
QUALITIES = ["low", "medium", "high", "auto"]


def generate_image(
    prompt: str,
    output_path: str = "output.png",
    size: str = "1024x1024",
    quality: Literal["low", "medium", "high", "auto"] = "medium",
) -> Path:
    client = OpenAI()

    print("[*] Sending prompt, waiting for gpt-image-2...")
    print(f"    Size   : {size}  Quality: {quality}")

    result = client.images.generate(
        model="gpt-image-2",
        prompt=prompt,
        size=size,
        quality=quality,
    )

    image_b64 = result.data[0].b64_json
    assert image_b64, "API 未回傳圖片資料"
    image_bytes = base64.b64decode(image_b64)

    out = Path(output_path)
    out.write_bytes(image_bytes)

    print(f"[+] Saved: {out.resolve()}")
    return out


if __name__ == "__main__":
    if not os.environ.get("OPENAI_API_KEY"):
        print("[-] Error: OPENAI_API_KEY not set. Add it to .env or set as environment variable.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="gpt-image-2 終端機產圖工具")
    parser.add_argument("-o", "--output", default="output.png", help="輸出檔名 (預設: output.png)")
    parser.add_argument("-s", "--size", default="1024x1024", choices=SIZES, help="圖片尺寸")
    parser.add_argument("-q", "--quality", default="medium", choices=QUALITIES, help="畫質")
    args = parser.parse_args()

    generate_image(PROMPT, args.output, args.size, args.quality)
