# tranquil-canvas

透過 OpenAI `gpt-image-2` 模型從終端機生成圖片的極簡 CLI 工具。

把提示詞存成 `.txt` 或 `.md` 放進 `input/`，執行 `main.py`，圖片會輸出到 `output/`。

## 環境需求

- Python 3.10+
- OpenAI API 金鑰（需完成組織驗證才能使用 `gpt-image-2`）

## 安裝

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS / Linux

pip install -r requirements.txt
```

在專案根目錄建立 `.env`：

```dotenv
OPENAI_API_KEY=sk-proj-...
```

## 使用方式

編輯 `input/prompt.txt`，然後執行：

```bash
python main.py
```

圖片輸出到 `output/output.png`。

### 參數說明

| 參數 | 預設值 | 說明 |
| ---- | ------ | ---- |
| `-p`, `--prompt-file` | `input/prompt.txt` | prompt 文字檔路徑；只輸入檔名時自動從 `input/` 尋找 |
| `-b`, `--batch-file` | — | 批次模式 prompt 檔；支援 `.txt` 或 `.md` |
| `--style-file` | — | 批次模式外部共用 style prompt 檔 |
| `--batch-prefix` | `image` | 批次模式未指定檔名時的輸出前綴 |
| `--image` | — | 批次模式只輸出指定的第幾張（從 1 開始） |
| `--images` | — | 批次模式只輸出指定的幾張，逗號分隔，例如 `8,11,13` |
| `--from-image` | — | 批次模式從指定張數開始一路輸出到最後 |
| `--range` | — | 批次模式只輸出指定範圍，例如 `2-5` |
| `--skip-images` | — | 批次模式跳過指定張數，例如 `3,7,9` |
| `-o`, `--output` | `output.png` | 輸出檔名（自動存到 `--output-dir`） |
| `--output-dir` | `output` | 輸出資料夾 |
| `-s`, `--size` | `1024x1024` | 圖片尺寸 |
| `-q`, `--quality` | `medium` | 畫質 |

### 尺寸選項

| 尺寸 | 類型 | 備註 |
| ---- | ---- | ---- |
| `1024x1024` | 正方形 | 生成最快，最省錢 |
| `1440x1440` | 正方形 | 中等解析度正方形 |
| `1536x1088` | 橫式 A2 | |
| `1088x1536` | 直式 A2 | |
| `1536x1024` | 橫式 3:2 | |
| `1024x1536` | 直式 2:3 | |
| `2048x1440` | 橫式 A2 高解析 | |
| `1440x2048` | 直式 A2 高解析 | |
| `2048x1152` | **橫式 16:9** | 桌面桌布、影片封面 |
| `1152x2048` | **直式 9:16** | 海報、手機桌布 |
| `2048x2048` | 2K 正方形 | 實驗性 |
| `3840x2720` | 橫式 A2 超高解析 | 實驗性 |
| `2720x3840` | 直式 A2 超高解析 | 實驗性 |
| `3840x2160` | 4K 橫式 | 實驗性 |
| `2160x3840` | 4K 直式 | 實驗性，最大解析度 |

> 限制：最大邊 3840px，長寬比不超過 3:1，尺寸須為 16px 的倍數。

### 畫質選項

| 畫質 | 速度 | 說明 |
| ---- | ---- | ---- |
| `low` | 最快 | 草稿與 prompt 測試 |
| `medium` | 中等 | 速度與品質的平衡點 |
| `high` | 最慢 | 細節最豐富 |
| `auto` | — | 由模型自動決定 |

### 範例

```bash
# 指定 prompt 與輸出檔名
python main.py -p yue-lingshan.txt -o yue-lingshan.png

# 指定輸出資料夾
python main.py -p yue-lingshan.txt --output-dir output/drafts -o draft.png

# 快速草稿（最省錢）
python main.py -q low -o draft.png

# A2 直式海報 — 先草稿確認構圖，再升解析度
python main.py -p yue-lingshan.txt -s 1088x1536 -q medium -o a2_medium.png
python main.py -p yue-lingshan.txt -s 1440x2048 -q high   -o a2_high.png
python main.py -p yue-lingshan.txt -s 2720x3840 -q high   -o a2_ultra.png

# 9:16 直式（海報、手機桌布）
python main.py -s 1152x2048 -q low  -o draft.png
python main.py -s 1152x2048 -q high -o portrait_final.png

# 16:9 橫式（桌面桌布、影片封面）
python main.py -s 2048x1152 -q high -o landscape.png

# 批次模式：.txt 每行一張圖
python main.py -b infographic-lines.txt -s 1024x1024 -q low --output-dir output/infographic

# 批次模式：.md 的 style + image 區塊
python main.py -b infographic-example.md -s 1024x1024 -q low --output-dir output/infographic

# 批次模式：只重跑第 5 張
python main.py -b infographic_God_Complex.md --image 5 -s 1024x1024 -q low --output-dir output/infographic_god_complex

# 批次模式：只重跑指定的幾張（不連續）
python main.py -b infographic_God_Complex.md --images 8,11,13 -s 1024x1024 -q low --output-dir output/infographic_god_complex

# 批次模式：從第 5 張開始一路重跑到最後
python main.py -b infographic_God_Complex.md --from-image 5 -s 1024x1024 -q low --output-dir output/infographic_god_complex

# 批次模式：只重跑第 2 到第 5 張
python main.py -b infographic_God_Complex.md --range 2-5 -s 1024x1024 -q low --output-dir output/infographic_god_complex

# 批次模式：全部重跑，但跳過第 3、7、9 張
python main.py -b infographic_God_Complex.md --skip-images 3,7,9 -s 1024x1024 -q low --output-dir output/infographic_god_complex

# 2K / 4K（實驗性）
python main.py -s 2048x2048 -q high -o 2k.png
python main.py -s 2160x3840 -q high -o 4k.png
python main.py -s 3840x2160 -q high -o 4k_landscape.png
```

## 批次模式

### `.txt` 格式

每行一張圖，可用 `檔名|prompt` 指定輸出檔名，`#` 開頭的行會被略過：

```text
sunrise over a misty mountain
city_night|neon-lit street at night, cyberpunk style
```

### `.md` 格式

用 `# style` 定義共用風格，`# image xx` 定義每張圖的內容：

````md
# style
```
整體風格是乾淨的 infographic、扁平設計、統一配色...
```

# image 01
```
主題：什麼是過敏
重點：三個症狀、簡單圖示、清楚標題
```

# image 02
```
主題：常見誘因
重點：食物、塵蟎、花粉...
```
````

執行時每張圖會自動合併 `# style` + 對應的 `# image` 區塊再送出，
區塊內容可選擇包在 ` ``` ` 代碼塊內，程式會自動去除外層符號。

## 費用參考（gpt-image-2）

官方標準尺寸定價：

| 畫質 | 1024×1024 | 1024×1536 | 1536×1024 |
| ---- | --------- | --------- | --------- |
| `low` | $0.006 | $0.005 | $0.005 |
| `medium` | $0.053 | $0.041 | $0.041 |
| `high` | $0.211 | $0.165 | $0.165 |

- 高於 1536 的實驗性尺寸（2048、3840 系列）不在官方定價表，但成本明顯更高。
- 最省錢的穩定草稿尺寸：`1024x1024` + `low`（$0.006/張）。
- 實際費用 = 圖片輸出 token + prompt input token，使用參考圖或局部編輯還需加計 input image token。
- 複雜提示詞最長可能需要接近 2 分鐘。

## 專案結構

```text
tranquil-canvas/
├── input/
│   └── prompt.txt   # 在這裡修改提示詞
├── output/          # 生成的圖片會放在這裡
├── main.py
└── requirements.txt
```

## 授權

MIT
