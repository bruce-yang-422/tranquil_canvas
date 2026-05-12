# tranquil-canvas

透過 OpenAI `gpt-image-2` 模型從終端機生成圖片的極簡 CLI 工具。

把提示詞存成 `.txt` 放進 `input/`，執行 `main.py`，圖片會輸出到 `output/`。

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

先編輯 `input/prompt.txt`，然後執行：

```bash
python main.py
```

### 參數說明

| 參數 | 預設值 | 說明 |
| ---- | ------ | ---- |
| `-p`, `--prompt-file` | `input/prompt.txt` | prompt 文字檔路徑；只輸入檔名時會自動從 `input/` 尋找 |
| `-o`, `--output` | `output.png` | 輸出檔名（預設存到 `output/`） |
| `--output-dir` | `output` | 輸出資料夾 |
| `-s`, `--size` | `1024x1024` | 圖片尺寸（目前僅支援固定尺寸，不支援 `auto`） |
| `-q`, `--quality` | `medium` | 畫質 |

### 尺寸選項

| 尺寸 | 類型 | 備註 |
| ---- | ---- | ---- |
| `1024x1024` | 正方形 | 生成最快 |
| `1536x1088` | 橫式 A2 比例 | 適合 `medium` / `high` |
| `1088x1536` | 直式 A2 比例 | 適合 `medium` / `high` |
| `1536x1024` | 橫式 3:2 | |
| `1024x1536` | 直式 2:3 | |
| `2048x1440` | 橫式 A2 比例 | 高解析海報 |
| `1440x2048` | 直式 A2 比例 | 高解析海報 |
| `2048x1152` | **16:9 橫式** | 最接近 16:9，適合桌面/影片封面 |
| `1152x2048` | **9:16 直式** | 最接近 9:16，適合海報/手機桌布 |
| `2048x2048` | 2K 正方形 | 實驗性功能 |
| `3840x2720` | 橫式 A2 比例 | 實驗性超高解析 |
| `2720x3840` | 直式 A2 比例 | 實驗性超高解析 |
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
# 預設讀取 input/prompt.txt，輸出到 output/output.png
python main.py

# 只指定輸出檔名，會自動存到 output/my_image.png
python main.py -o my_image.png

# 指定另一個 prompt 檔案，只輸入檔名即可
python main.py -p yue-lingshan.txt -o yue-lingshan.png

# 指定 prompt 與輸出檔名，兩者都不用完整路徑
python main.py -p wuxia_poster.txt -o poster_v1.png

# 指定輸出資料夾
python main.py -p yue-lingshan.txt --output-dir output/drafts -o draft.png

# 最便宜的合法草稿尺寸：1024x1024
python main.py -p yue-lingshan.txt -s 1024x1024 -q low -o cheap_square_draft.png

# A2 直式海報，medium 畫質
python main.py -p yue-lingshan.txt -s 1088x1536 -q medium -o a2_poster_medium.png

# A2 直式海報，high 畫質
python main.py -p yue-lingshan.txt -s 1440x2048 -q high -o a2_poster_high.png

# A2 直式海報，超高解析（實驗性）
python main.py -p yue-lingshan.txt -s 2720x3840 -q high -o a2_poster_ultra.png

# 2:3 直式海報，高畫質
python main.py -s 1024x1536 -q high -o poster.png

# 9:16 直式（海報、手機桌布）— 先草稿確認後再出正式版
python main.py -s 1152x2048 -q low -o draft.png
python main.py -s 1152x2048 -q high -o portrait_final.png

# 16:9 橫式（桌面桌布、影片封面）
python main.py -s 2048x1152 -q high -o landscape.png

# 3:2 橫式，高畫質
python main.py -s 1536x1024 -q high -o banner.png

# 快速草稿（最省錢，適合測試 prompt）
python main.py -q low -o draft.png

# 2K 正方形
python main.py -s 2048x2048 -q high -o 2k.png

# 4K 直式（最大解析度，實驗性）
python main.py -s 2160x3840 -q high -o 4k.png

# 4K 橫式（實驗性）
python main.py -s 3840x2160 -q high -o 4k_landscape.png

# 讓模型自動決定畫質
python main.py -q auto -o auto_quality.png
```

## 專案結構

```text
tranquil-canvas/
├── input/
│   └── prompt.txt   # 在這裡修改提示詞
├── output/          # 生成的圖片會放在這裡
├── main.py          # 主程式
├── requirements.txt
└── .env             # API 金鑰（不納入版控）
```

## 費用參考（gpt-image-2）

以下是文件中的官方參考價格：

| 畫質 | 1024×1024 | 1024×1536 | 1536×1024 |
| ---- | --------- | --------- | --------- |
| `low` | $0.006 | $0.005 | $0.005 |
| `medium` | $0.053 | $0.041 | $0.041 |
| `high` | $0.211 | $0.165 | $0.165 |

對應的輸出 token 參考如下：

| 畫質 | 1024×1024 | 1024×1536 | 1536×1024 |
| ---- | --------- | --------- | --------- |
| `low` | 272 tokens | 408 tokens | 400 tokens |
| `medium` | 1056 tokens | 1584 tokens | 1568 tokens |
| `high` | 4160 tokens | 6240 tokens | 6208 tokens |

補充說明：

- 你目前程式支援的 `2048x1152`、`1152x2048`、`2048x2048`、`3840x2160`、`2160x3840` 並沒有在這份文件裡看到官方固定價目表，但可以合理判斷成本會高於 1024 / 1536 級別。
- 低於 1024×1024 像素量級的尺寸目前會被 API 拒絕，所以最便宜的穩定草稿尺寸建議從 `1024x1024` 開始。
- 如果你要做 A2 海報，建議先用 `1088x1536` 的 `medium`，再升到 `1440x2048` 或 `2720x3840` 的 `high`。
- `low` 很適合拿來做草稿與 prompt 測試，通常最省錢。
- 實際總成本不只圖片輸出，還包含 prompt 的 `input text tokens`。
- 如果之後加上參考圖或編輯圖片，還會再加上 `input image tokens` 成本。
- 複雜提示詞最長可能需要接近 2 分鐘。

## 授權

MIT
