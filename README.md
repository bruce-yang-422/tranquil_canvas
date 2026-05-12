# tranquil-canvas

透過 OpenAI `gpt-image-2` 模型從終端機生成圖片的極簡 CLI 工具。

在 `prompt.py` 裡寫好提示詞，執行 `main.py`，取得圖片。

## 環境需求

- Python 3.10+
- OpenAI API 金鑰（需完成組織驗證才能使用 `gpt-image-2`）

## 安裝

```bash
# 建立並啟動虛擬環境
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS / Linux

# 安裝套件
pip install -r requirements.txt
```

在專案根目錄建立 `.env` 檔案：

```dotenv
OPENAI_API_KEY=sk-proj-...
```

## 使用方式

編輯 `prompt.py` 設定提示詞，然後執行：

```bash
python main.py
```

### 參數說明

| 參數 | 預設值 | 說明 |
| ---- | ------ | ---- |
| `-o`, `--output` | `output.png` | 輸出檔名 |
| `-s`, `--size` | `1024x1024` | 圖片尺寸 |
| `-q`, `--quality` | `medium` | 畫質 |

### 尺寸選項

| 尺寸 | 類型 | 備註 |
| ---- | ---- | ---- |
| `1024x1024` | 正方形 | 生成最快 |
| `1536x1024` | 橫式 3:2 | |
| `1024x1536` | 直式 2:3 | |
| `2048x1152` | **16:9 橫式** | 最接近 16:9，適合桌面/影片封面 |
| `1152x2048` | **9:16 直式** | 最接近 9:16，適合海報/手機桌布 |
| `2048x2048` | 2K 正方形 | 實驗性功能 |
| `3840x2160` | 4K 橫式 | 實驗性功能 |
| `2160x3840` | 4K 直式 | 實驗性功能，最大解析度 |

### 畫質選項

| 畫質 | 速度 | 說明 |
| ---- | ---- | ---- |
| `low` | 最快 | 適合草稿與快速測試 |
| `medium` | 中等 | 平衡速度與品質 |
| `high` | 最慢 | 細節最豐富 |
| `auto` | — | 由模型自動決定 |

### 範例

```bash
# 預設（1024x1024，medium 畫質）
python main.py

# 指定輸出檔名
python main.py -o my_image.png

# 直式海報，高畫質
python main.py -s 1024x1536 -q high -o poster.png

# 9:16 直式（海報、手機桌布）— 先草稿確認後再出正式版
python main.py -s 1152x2048 -q low -o draft.png
python main.py -s 1152x2048 -q high -o portrait_final.png

# 16:9 橫式（桌面桌布、影片封面）
python main.py -s 2048x1152 -q high -o landscape.png

# 橫式寬幅，高畫質
python main.py -s 1536x1024 -q high -o banner.png

# 快速草稿（最省錢，適合測試 prompt）
python main.py -q low -o draft.png

# 2K 正方形
python main.py -s 2048x2048 -q high -o 2k.png

# 2K 直式
python main.py -s 1152x2048 -q high -o 2k_portrait.png

# 4K 直式（最大解析度，實驗性）
python main.py -s 2160x3840 -q high -o 4k.png

# 4K 橫式（實驗性）
python main.py -s 3840x2160 -q high -o 4k_landscape.png

# 讓模型自動決定畫質與尺寸
python main.py -s auto -q auto -o auto.png
```

## 專案結構

```text
tranquil-canvas/
├── main.py          # 主程式
├── prompt.py        # 在這裡修改提示詞
├── requirements.txt
├── .env             # API 金鑰（不納入版控）
└── output.png       # 生成的圖片
```

## 費用參考（gpt-image-2）

| 畫質   | 1024×1024 | 1024×1536 | 1536×1024 |
|--------|-----------|-----------|-----------|
| low    | $0.006    | $0.005    | $0.005    |
| medium | $0.053    | $0.041    | $0.041    |
| high   | $0.211    | $0.165    | $0.165    |

實驗性高解析度尺寸費用會更高，複雜提示詞最長可能需要 2 分鐘。

## 授權

MIT
