"""
infographic.py — 用 Pillow 生成「陪伴憂鬱同事」系列資訊圖表
生成 5 張 1080×1920 PNG，存至 output/infographic/
"""

from __future__ import annotations
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageFont

W, H = 1080, 1920
MARGIN = 72
CONTENT_W = W - MARGIN * 2
OUTPUT_DIR = Path("output/infographic")
DECOR_DIR  = Path("output/decorations")

# ── 色盤 ─────────────────────────────────────────────────
MINT       = (174, 203, 186)  # #AECBBA
FOG_GREEN  = (212, 224, 214)  # #D4E0D6
PALE_GRN   = (232, 241, 233)  # #E8F1E9
GRN_DARK   = (76, 116, 90)
FROST_BLU  = (224, 232, 240)  # #E0E8F0
DUSTY_BLU  = (181, 198, 217)  # #B5C6D9
BLU_DARK   = (65, 98, 145)
CREAM_YLW  = (255, 250, 205)  # #FFFACD
SOFT_YLW   = (253, 244, 197)  # #FDF4C5
YLW_DARK   = (155, 128, 48)
PEACH      = (255, 218, 185)  # #FFDAB9
SOFT_ORG   = (250, 220, 200)  # #FADCC8
PCH_DARK   = (185, 105, 65)
SKY_BLU    = (201, 214, 234)  # #C9D6EA
SKY_DARK   = (62, 92, 142)
WHITE      = (255, 255, 255)
DARK_TXT   = (61, 61, 61)
MID_TXT    = (90, 90, 90)
LIGHT_TXT  = (136, 136, 136)

# ── 字型路徑 ─────────────────────────────────────────────
_USER_FONTS = Path("C:/Users/bruce/AppData/Local/Microsoft/Windows/Fonts")
_SYS_FONTS  = Path("C:/Windows/Fonts")

_HEAVY      = str(_USER_FONTS / "jf-jinxuan-3.1-heavy.otf")   # jf 金萱 Heavy → 主標題
_ROUND      = str(_USER_FONTS / "jf-openhuninn-2.0.ttf")      # jf open粉圓   → 次標題/內文/badge
_NOTO       = str(_USER_FONTS / "NotoSansCJKtc-Regular.otf")  # Noto 思源     → 小字說明
_HANDWRITE  = str(_USER_FONTS / "creamfont-3.2.otf")    # 凝書體 → 頁尾溫暖備註
_FALLBACK   = str(_SYS_FONTS  / "msjh.ttc")                   # 微軟正黑體    → 萬用備援


def _font(path: str, size: int) -> ImageFont.FreeTypeFont:
    p = Path(path)
    src = str(p) if p.exists() else _FALLBACK
    return ImageFont.truetype(src, size)


def build_fonts() -> dict[str, ImageFont.FreeTypeFont]:
    return {
        "h1":        _font(_HEAVY,     62),
        "h2":        _font(_ROUND,     44),
        "body":      _font(_ROUND,     36),
        "small":     _font(_NOTO,      30),
        "badge":     _font(_ROUND,     28),
        "handwrite": _font(_HANDWRITE, 39),
    }


# ── 排版工具 ──────────────────────────────────────────────
def wrap(text: str, font: ImageFont.FreeTypeFont, max_w: int,
         draw: ImageDraw.ImageDraw) -> list[str]:
    lines: list[str] = []
    for para in text.split("\n"):
        if not para:
            lines.append("")
            continue
        cur = ""
        for ch in para:
            test = cur + ch
            if draw.textlength(test, font=font) > max_w and cur:
                lines.append(cur)
                cur = ch
            else:
                cur = test
        if cur:
            lines.append(cur)
    return lines


def draw_lines(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    color: tuple,
    x: int,
    y: int,
    align: str = "left",
    line_gap: int = 10,
    ref_w: int = CONTENT_W,
) -> int:
    for line in lines:
        if not line:
            y += font.size // 2
            continue
        lw = int(draw.textlength(line, font=font))
        tx = x + (ref_w - lw) // 2 if align == "center" else x
        draw.text((tx, y), line, font=font, fill=color)
        y += font.size + line_gap
    return y


def pill(draw: ImageDraw.ImageDraw, cx: int, y: int, text: str,
         font: ImageFont.FreeTypeFont, bg: tuple, fg: tuple) -> int:
    lw = int(draw.textlength(text, font=font))
    ph, pv = 28, 10
    bw = lw + ph * 2
    bh = font.size + pv * 2
    x1 = cx - bw // 2
    draw.rounded_rectangle([x1, y, x1 + bw, y + bh], radius=bh // 2, fill=bg)
    draw.text((x1 + ph, y + pv), text, font=font, fill=fg)
    return y + bh


def hline(draw: ImageDraw.ImageDraw, y: int, color: tuple) -> None:
    draw.line([MARGIN, y, W - MARGIN, y], fill=color, width=2)


def remove_white_bg(img: Image.Image, tolerance: int = 20) -> Image.Image:
    """把接近白色的像素變透明，tolerance 控制柔和過渡範圍（各通道偏離 255 的最大距離）。"""
    img = img.convert("RGBA")
    white = Image.new("RGB", img.size, (255, 255, 255))
    diff = ImageChops.difference(img.convert("RGB"), white)
    dr, dg, db = diff.split()
    max_diff = ImageChops.lighter(ImageChops.lighter(dr, dg), db)

    def diff_to_alpha(v: int) -> int:
        if v <= tolerance:
            return round(v * 255 / tolerance) if tolerance > 0 else 0
        return 255

    computed_a = max_diff.point(diff_to_alpha)
    _, _, _, orig_a = img.split()
    img.putalpha(ImageChops.darker(computed_a, orig_a))
    return img


def paste_decor(
    canvas: Image.Image,
    name: str,
    target_w: int,
    x: int,
    y: int,
    alpha: int = 200,
    debg: bool = True,
) -> None:
    """將裝飾插圖合成到畫布上。name 對應 output/decorations/<name>.png。
    找不到檔案時直接跳過，不報錯。
    debg: True 時自動去除白色背景。
    alpha: 0=全透明, 255=完全不透明。
    """
    path = DECOR_DIR / f"{name}.png"
    if not path.exists():
        return

    decor = Image.open(path).convert("RGBA")

    if debg:
        decor = remove_white_bg(decor)

    aspect = decor.height / decor.width
    new_size = (target_w, round(target_w * aspect))
    decor = decor.resize(new_size, Image.Resampling.LANCZOS)

    if alpha < 255:
        scale = alpha / 255
        decor.putalpha(decor.getchannel("A").point(lambda v: round(v * scale)))

    canvas.paste(decor, (x, y), decor)


def dot_text(draw: ImageDraw.ImageDraw, cx: int, cy: int, r: int,
             text: str, font: ImageFont.FreeTypeFont, bg: tuple) -> None:
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=bg)
    lw = int(draw.textlength(text, font=font))
    draw.text((cx - lw // 2, cy - font.size // 2), text, font=font, fill=WHITE)


# ── 卡片元件 ──────────────────────────────────────────────
def step_card(
    draw: ImageDraw.ImageDraw,
    fonts: dict,
    y: int,
    number: str,
    label: str,
    body: str,
    card_bg: tuple,
    dot_color: tuple,
) -> int:
    pad, dot_r = 26, 30
    dot_cx = MARGIN + pad + dot_r
    title_x = dot_cx + dot_r + 18
    inner_w = W - MARGIN - title_x - pad

    title_lines = wrap(label, fonts["h2"], inner_w, draw)
    body_lines = wrap(body, fonts["small"], inner_w, draw)

    title_h = len(title_lines) * (fonts["h2"].size + 6)
    body_h = len(body_lines) * (fonts["small"].size + 6)
    inner_h = max(dot_r * 2, title_h + 8 + body_h)
    card_h = pad + inner_h + pad

    draw.rounded_rectangle([MARGIN, y, W - MARGIN, y + card_h], radius=18, fill=card_bg)

    dot_cy = y + pad + dot_r
    dot_text(draw, dot_cx, dot_cy, dot_r, number, fonts["h2"], dot_color)

    ty = y + pad
    for line in title_lines:
        draw.text((title_x, ty), line, font=fonts["h2"], fill=DARK_TXT)
        ty += fonts["h2"].size + 6
    ty += 8
    for line in body_lines:
        draw.text((title_x, ty), line, font=fonts["small"], fill=MID_TXT)
        ty += fonts["small"].size + 6

    return y + card_h


def tip_card(
    draw: ImageDraw.ImageDraw,
    fonts: dict,
    y: int,
    number: str,
    title: str,
    body: str,
    dot_color: tuple,
) -> int:
    pad, dot_r = 24, 28
    dot_cx = MARGIN + pad + dot_r
    dot_cy = y + pad + dot_r
    inner_x = dot_cx + dot_r + 16
    inner_w = W - MARGIN - inner_x - pad

    body_lines = wrap(body, fonts["small"], inner_w, draw)
    card_h = pad + max(dot_r * 2, fonts["h2"].size + 8 + len(body_lines) * (fonts["small"].size + 6)) + pad

    draw.rounded_rectangle([MARGIN, y, W - MARGIN, y + card_h], radius=16, fill=WHITE)
    dot_text(draw, dot_cx, dot_cy, dot_r, number, fonts["badge"], dot_color)

    draw.text((inner_x, y + pad), title, font=fonts["h2"], fill=DARK_TXT)

    by = y + pad + fonts["h2"].size + 8
    for line in body_lines:
        draw.text((inner_x, by), line, font=fonts["small"], fill=MID_TXT)
        by += fonts["small"].size + 6

    return y + card_h


def compassion_card(
    draw: ImageDraw.ImageDraw,
    fonts: dict,
    y: int,
    title: str,
    body: str,
    accent: tuple,
) -> int:
    pad = 32
    inner_x = MARGIN + 20
    inner_w = CONTENT_W - 20

    body_lines = wrap(body, fonts["body"], inner_w - pad, draw)
    card_h = pad + fonts["h2"].size + 14 + len(body_lines) * (fonts["body"].size + 10) + pad

    draw.rounded_rectangle([MARGIN, y, W - MARGIN, y + card_h], radius=22, fill=WHITE)
    draw.rectangle([MARGIN, y + 20, MARGIN + 7, y + card_h - 20], fill=accent)

    draw.text((inner_x + pad, y + pad), title, font=fonts["h2"], fill=accent)
    by = y + pad + fonts["h2"].size + 14
    for line in body_lines:
        draw.text((inner_x + pad, by), line, font=fonts["body"], fill=MID_TXT)
        by += fonts["body"].size + 10

    return y + card_h


def hotline_card(
    draw: ImageDraw.ImageDraw,
    fonts: dict,
    y: int,
    number: str,
    name: str,
    desc: str,
    accent: tuple,
) -> int:
    pad = 28
    lpad = 36

    name_lines = wrap(name, fonts["h2"], CONTENT_W - lpad * 2, draw)
    desc_lines = wrap(desc, fonts["small"], CONTENT_W - lpad * 2, draw)
    card_h = (pad
              + fonts["h1"].size + 8
              + len(name_lines) * (fonts["h2"].size + 6)
              + len(desc_lines) * (fonts["small"].size + 6)
              + pad)

    draw.rounded_rectangle([MARGIN, y, W - MARGIN, y + card_h], radius=18, fill=WHITE)
    draw.rectangle([MARGIN, y + 20, MARGIN + 7, y + card_h - 20], fill=accent)

    tx = MARGIN + lpad
    draw.text((tx, y + pad), number, font=fonts["h1"], fill=accent)
    ty = y + pad + fonts["h1"].size + 8
    for line in name_lines:
        draw.text((tx, ty), line, font=fonts["h2"], fill=DARK_TXT)
        ty += fonts["h2"].size + 6
    for line in desc_lines:
        draw.text((tx, ty), line, font=fonts["small"], fill=LIGHT_TXT)
        ty += fonts["small"].size + 6

    return y + card_h


# ── 五張圖表 ─────────────────────────────────────────────

def make_chart_1(fonts: dict) -> Image.Image:
    img = Image.new("RGB", (W, H), PALE_GRN)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 14], fill=MINT)

    y = 72
    y = pill(draw, W // 2, y, "急性情緒急救包", fonts["badge"], MINT, DARK_TXT) + 36

    for t in ["感到被情緒淹沒了嗎？", "讓我們一起回到現在。"]:
        lw = int(draw.textlength(t, font=fonts["h1"]))
        draw.text(((W - lw) // 2, y), t, font=fonts["h1"], fill=DARK_TXT)
        y += fonts["h1"].size + 10
    y += 24

    intro = "這是一個簡單的感官練習，幫助大腦在混亂中找到平靜。\n跟著步驟，慢慢來，深吸一口氣......"
    y = draw_lines(draw, wrap(intro, fonts["body"], CONTENT_W, draw),
                   fonts["body"], MID_TXT, MARGIN, y, align="center") + 32

    steps = [
        ("5", "看見 5 樣",
         "環顧四周，說出 5 件你能看見的事物。\n例如：植物、海報、天花板、窗外的天空、桌上的杯子。"),
        ("4", "觸摸 4 樣",
         "感受 4 件你摸得到的事物。\n例如：腳底的溫暖、衣服的質地、椅背的支撐。"),
        ("3", "聆聽 3 種",
         "注意 3 種你能聽到的聲音。\n例如：遠處的車聲、時鐘滴答聲、冷氣低鳴。"),
        ("2", "嗅聞 2 種",
         "尋找 2 種你聞得到的氣味。\n聞不到的話，就想像你最喜歡的兩種香味。"),
        ("1", "感受 1 種味道",
         "留意嘴裡的味道，或想像最愛食物的滋味。"),
    ]
    bgs = [MINT, FOG_GREEN, FOG_GREEN, PALE_GRN, (220, 234, 224)]

    for i, (num, label, body) in enumerate(steps):
        y = step_card(draw, fonts, y, num, label, body, bgs[i], GRN_DARK) + 14

    footer_y = H - 160
    hline(draw, footer_y, MINT)
    footer_y += 22
    footer = "做得很好。思緒飄走了也沒關係，可以隨時重來。\n我會陪著你慢慢呼吸。"
    draw_lines(draw, wrap(footer, fonts["handwrite"], CONTENT_W, draw),
               fonts["handwrite"], GRN_DARK, MARGIN, footer_y, align="center", line_gap=14)

    paste_decor(img, "decor_01_plant", target_w=300, x=W - 320, y=H - 420, alpha=170)
    return img


def make_chart_2(fonts: dict) -> Image.Image:
    img = Image.new("RGB", (W, H), FROST_BLU)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 14], fill=DUSTY_BLU)

    y = 72
    y = pill(draw, W // 2, y, "著陸技術擴充包", fonts["badge"], DUSTY_BLU, DARK_TXT) + 36

    for t in ["遠離情緒風暴的", "10 個著陸小技巧"]:
        lw = int(draw.textlength(t, font=fonts["h1"]))
        draw.text(((W - lw) // 2, y), t, font=fonts["h1"], fill=DARK_TXT)
        y += fonts["h1"].size + 10
    y += 32

    tips = [
        ("01", "手放入水中",   "感受水流過手指的溫度，專注在皮膚的感受。"),
        ("02", "握緊再放開",   "握拳感受壓力，維持幾秒後慢慢放開，有需要時重複。"),
        ("03", "寵物陪伴",    "輕撫寵物，專注感受牠的毛髮、呼吸與體溫。"),
        ("04", "大腦分類遊戲", "選一個類別，1 分鐘內在腦海列出所有項目。\n例如：水果——香蕉、蘋果、草莓......"),
        ("05", "重新定位當下", "說出你的名字、年齡、現在的位置與時間。"),
        ("06", "預演日常步驟", "在腦海仔細預演一件常做的事，\n例如泡咖啡的每一個細節。"),
    ]

    for num, title, body in tips:
        y = tip_card(draw, fonts, y, num, title, body, DUSTY_BLU) + 16

    footer_y = max(y + 16, H - 140)
    hline(draw, footer_y, DUSTY_BLU)
    footer_y += 22
    footer = "試試看哪一個最適合你，找到屬於你的平靜開關。"
    draw_lines(draw, wrap(footer, fonts["handwrite"], CONTENT_W, draw),
               fonts["handwrite"], BLU_DARK, MARGIN, footer_y, align="center")

    paste_decor(img, "decor_02_water", target_w=280, x=W - 300, y=H - 380, alpha=160)
    return img


def make_chart_3(fonts: dict) -> Image.Image:
    img = Image.new("RGB", (W, H), CREAM_YLW)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 14], fill=SOFT_YLW)

    y = 110
    y = pill(draw, W // 2, y, "存在危機緩解卡", fonts["badge"], SOFT_YLW, DARK_TXT) + 72

    t = "關於「活著的意義」..."
    lw = int(draw.textlength(t, font=fonts["h1"]))
    draw.text(((W - lw) // 2, y), t, font=fonts["h1"], fill=DARK_TXT)
    y += fonts["h1"].size + 72

    paras = [
        ("body",  MID_TXT,  "大腦生病的時候，\n思緒容易走進灰色的迷宮。"),
        ("body",  MID_TXT,  "我們都是在這個星球上第一次體驗人生，\n沒有經驗是正常的，\n現在找不到答案也是非常正常的。"),
        ("h2",    DARK_TXT, "今天，我們不需要急著\n去尋找生命宏大的意義。"),
        ("body",  MID_TXT,  "只要能夠好好呼吸、平安地度過今天，\n就已經是一件無比了不起的事了。"),
    ]

    for style, color, text in paras:
        font = fonts[style]
        lines = wrap(text, font, CONTENT_W, draw)
        for line in lines:
            lw_line = int(draw.textlength(line, font=font))
            draw.text(((W - lw_line) // 2, y), line, font=font, fill=color)
            y += font.size + 14
        y += 64

    hline(draw, y, SOFT_YLW)
    y += 48
    footer = "你的存在本身，對我來說就很有意義。\n不用急著找答案，我在這裡陪你慢慢走。"
    draw_lines(draw, wrap(footer, fonts["handwrite"], CONTENT_W, draw),
               fonts["handwrite"], YLW_DARK, MARGIN, y, align="center", line_gap=16)

    paste_decor(img, "decor_03_seedling", target_w=380, x=(W - 380) // 2, y=H - 480, alpha=180)
    return img


def make_chart_4(fonts: dict) -> Image.Image:
    img = Image.new("RGB", (W, H), PEACH)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 14], fill=SOFT_ORG)

    y = 80
    y = pill(draw, W // 2, y, "自我疼惜卡", fonts["badge"], SOFT_ORG, DARK_TXT) + 60

    t = "致  現在感到疲憊的你"
    lw = int(draw.textlength(t, font=fonts["h1"]))
    draw.text(((W - lw) // 2, y), t, font=fonts["h1"], fill=DARK_TXT)
    y += fonts["h1"].size + 60

    items = [
        ("這不是你的錯",
         "憂鬱就像大腦感冒，流眼淚只是身體在發燒。\n請不要為此感到抱歉。"),
        ("你絕對不是一個麻煩",
         "謝謝你這麼努力地撐到現在。\n你值得被理解，也值得被溫柔對待。"),
        ("允許自己停下腳步",
         "即使今天什麼都沒做也沒關係。\n好好休息，就是你現在最重要的任務。"),
    ]

    for title_item, body in items:
        y = compassion_card(draw, fonts, y, title_item, body, PCH_DARK) + 28

    hline(draw, y, SOFT_ORG)
    y += 28
    footer = "聽起來你現在很難受，這份痛苦是真實的，我聽到了。\n隨時傳個訊息給我，我會一直都在。"
    draw_lines(draw, wrap(footer, fonts["handwrite"], CONTENT_W, draw),
               fonts["handwrite"], PCH_DARK, MARGIN, y, align="center", line_gap=16)

    paste_decor(img, "decor_04_cloud", target_w=320, x=W - 340, y=H - 400, alpha=160)
    return img


def make_chart_5(fonts: dict) -> Image.Image:
    img = Image.new("RGB", (W, H), SKY_BLU)
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, W, 14], fill=DUSTY_BLU)

    y = 72
    y = pill(draw, W // 2, y, "醫療資源與安全網", fonts["badge"], DUSTY_BLU, DARK_TXT) + 36

    for t in ["覺得撐不下去的時候，", "我們一起找幫手。"]:
        lw = int(draw.textlength(t, font=fonts["h1"]))
        draw.text(((W - lw) // 2, y), t, font=fonts["h1"], fill=DARK_TXT)
        y += fonts["h1"].size + 10
    y += 24

    intro = "就像感冒看醫生、難題找專家，\n心理受傷了也可以尋求專業的協助。\n這代表你很勇敢。"
    y = draw_lines(draw, wrap(intro, fonts["body"], CONTENT_W, draw),
                   fonts["body"], MID_TXT, MARGIN, y, align="center") + 44

    hotlines = [
        ("1925", "安心專線（依舊愛我）",  "全年無休 24 小時，免費心理諮詢"),
        ("1995", "生命線協談專線",        "全年無休 24 小時"),
        ("1980", "張老師專線",            "全年無休，情緒困擾皆可撥"),
    ]

    for number, name, desc in hotlines:
        y = hotline_card(draw, fonts, y, number, name, desc, DUSTY_BLU) + 20

    y += 8
    draw.rounded_rectangle([MARGIN, y, W - MARGIN, y + 148], radius=16, fill=WHITE)
    draw.rectangle([MARGIN, y + 20, MARGIN + 7, y + 128], fill=SKY_DARK)
    draw.text((MARGIN + 36, y + 28), "衛生所心理諮詢", font=fonts["h2"], fill=SKY_DARK)
    draw.text((MARGIN + 36, y + 28 + fonts["h2"].size + 12),
              "各縣市衛生所提供免費心理諮商預約服務", font=fonts["small"], fill=MID_TXT)
    y += 148 + 56

    hline(draw, y, DUSTY_BLU)
    y += 28
    footer = "如果你覺得打電話太難，\n讓我陪你一起找資源，或者陪你去看醫生。\n你不是一個人面對。"
    draw_lines(draw, wrap(footer, fonts["handwrite"], CONTENT_W, draw),
               fonts["handwrite"], SKY_DARK, MARGIN, y, align="center", line_gap=14)

    paste_decor(img, "decor_05_hands", target_w=260, x=W - 280, y=H - 360, alpha=150)
    return img


# ── Main ────────────────────────────────────────────────
CHARTS = [
    ("01_grounding_54321",    make_chart_1),
    ("02_grounding_extra",    make_chart_2),
    ("03_existential_crisis", make_chart_3),
    ("04_self_compassion",    make_chart_4),
    ("05_safety_net",         make_chart_5),
]


def main() -> None:
    fonts = build_fonts()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for filename, make_fn in CHARTS:
        out = OUTPUT_DIR / f"{filename}.png"
        print(f"[*] 生成 {out.name} ...")
        img = make_fn(fonts)
        img.save(str(out))
        print(f"[+] 已儲存：{out.resolve()}")

    print(f"\n完成！共 {len(CHARTS)} 張圖存至 {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
