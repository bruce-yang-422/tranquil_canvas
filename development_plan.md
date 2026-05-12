# AI 圖像工具開發計畫

## 目前架構

採用「**CLI 終端機直接呼叫 API**」的輕量架構，省去 FastAPI 伺服器層。
提示詞統一寫在 `prompt.py`，`main.py` 負責呼叫 OpenAI 並將圖片存檔。

```text
prompt.py  →  main.py  →  gpt-image-2 API  →  output.png
```

---

## 階段一：CLI 單次產圖 MVP ✅ 已完成

**目標**：打通終端機 → API → 圖片存檔的完整流程。

- [x] 建立專案資料夾與虛擬環境 (`.venv`)
- [x] 安裝必備套件（`openai`, `python-dotenv`）
- [x] 建立 `.env` 儲存 API 金鑰
- [x] 撰寫 `main.py`，呼叫 `client.images.generate()` 並將 Base64 解碼存為 PNG
- [x] 撰寢 `prompt.py`，作為提示詞的獨立設定檔
- [x] 修正 `response_format` 參數問題（`gpt-image-2` 不支援，預設即回傳 b64_json）
- [x] 解決 Windows 終端機 cp950 編碼錯誤

---

## 階段二：CLI 參數化控制 ✅ 已完成

**目標**：讓使用者從終端機靈活控制輸出規格，無需修改原始碼。

- [x] 加入 `argparse`，支援 `-o`、`-s`、`-q` 三個參數
- [x] 尺寸選項涵蓋標準到 4K 共 8 種（含實驗性解析度）
- [x] 畫質選項：`low` / `medium` / `high` / `auto`
- [x] 輸出格式固定為 PNG（gpt-image-2 預設，無需額外設定）

---

## 階段三：專案規範化 ✅ 已完成

**目標**：建立可維護、可分享的專案基礎。

- [x] 撰寫 `README.md`（繁體中文，含安裝、用法、費用參考）
- [x] 建立 `.gitignore`（排除 `.env`、`.venv`、生成圖片）
- [x] 建立 `LICENSE`（MIT）
- [x] 更新 `requirements.txt`（含 `python-dotenv`）

---

## 階段四：前端網頁介面（待開發）

**目標**：提供視覺化操作介面，讓非技術使用者也能產圖。

- [ ] **步驟 1：FastAPI 後端**
  - 建立 `api.py`（獨立於現有 `main.py`）
  - 實作 `POST /api/generate` 端點，接收 prompt、size、quality
  - 設定 CORS，允許前端跨域請求
  - 回傳 Base64 圖片資料

- [ ] **步驟 2：前端靜態網頁 (`index.html`)**
  - 輸入框、尺寸/畫質下拉選單、送出按鈕
  - 圖片顯示區，載入中狀態提示
  - 用 `fetch` 呼叫 FastAPI，渲染回傳的 Base64 圖片

- [ ] **步驟 3：整合測試**
  - 啟動 `uvicorn api:app --reload`
  - 瀏覽器開啟 `index.html` 實測完整流程

---

## 階段五：進階功能（未來規劃）

**目標**：解鎖 `gpt-image-2` 完整潛力。

- [ ] **多輪對話（Responses API）**
  - 改用 `responses.create` 搭配 `previous_response_id`
  - 前端加入「以此圖修改」按鈕，傳遞 `image_call_id`
  - 測試迭代修改流程：畫 → 改細節 → 換背景

- [ ] **流式傳輸預覽（Streaming）**
  - 設定 `partial_images` 參數（0-3 張預覽）
  - 高畫質大圖等待期間先顯示低解析度進度圖

- [ ] **遮罩局部編輯（Inpainting）**
  - 上傳原圖與含 Alpha 通道的遮罩圖
  - 呼叫 `client.images.edit()` 實作指定區域替換
