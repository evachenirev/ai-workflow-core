# AI Workflow Core 中文產品規格書（PRD）

## 一、產品定位與目標

**AI Workflow Core** 是一套由模組化 AI 代理人構成的智慧工作流程平台，能協助使用者將初步構想（文字輸入）快速轉化為具結構的產品文檔與可執行任務。平台透過不同任務導向的提示詞（Prompt Templates），串接 OpenRouter 支援的語言模型（目前預設為 GPT-4）來完成任務拆解，未來也支援多模型擴充與開發工具整合。

### 🎯 主要目標客群
- 🚀 **初創團隊與產品經理**：快速構思產品原型並文檔化
- 🧑‍💻 **自由開發者**：從靈感出發迅速落地任務
- 🏢 **中小企業**：強化內部流程自動化與 KPI 架構規劃

## 二、功能模組總覽

| 模組名稱       | 功能說明 |
|----------------|----------|
| 💡 想法輸入     | 使用者以文字輸入原始構想（如："我要做一款庫存管理 App"） |
| 📄 PRD 模組     | 生成產品需求文件（Product Requirement Document） |
| 📊 調研模組     | 根據輸入主題產生市場競品分析、Persona 等資料 |
| ✅ 任務模組     | 拆解具體任務，包含優先順序與時程建議 |
| 🎯 KPI 模組     | 推導關鍵績效指標與評估方式 |
| 📂 輸出模組     | 將所有模組輸出以 Markdown 儲存，可下載或匯出至其他平台（規劃中） |

## 三、使用流程（User Flow）

1. 使用者透過 Streamlit 前端介面輸入想法
2. Controller 接收並分派輸入至各模組代理人（Agent）
3. 每個模組使用特定 Prompt 與 LLM（經由 OpenRouter）完成任務
4. 系統回傳 PRD、競品研究、任務拆解、KPI 建議等結果
5. 使用者可進行編輯與導出

## 四、技術架構概覽

📄 詳細架構圖請見 `docs/architecture.md`

- **前端介面**：基於 Streamlit，支援基本文字互動與結果展示
- **模型調度**：使用單一 LLM（GPT-4 via OpenRouter），配合多類任務型 Prompt 實現模擬多代理人架構
- **模組結構**：各功能模組獨立封裝於 `src/agents/`，便於擴充與測試
- **快取策略**：目前支援本地儲存與 SQLite 快取（Redis 規劃中）
- **資料儲存**：所有輸出存於 `/outputs/` 資料夾，依時間戳命名

## 五、產品開發路線（MVP 與後續）

| 狀態 | 功能項目 |
|------|----------|
| ✅   | PRD、Research、Task、KPI 模組基本功能已完成 |
| ✅   | 多語言輸入支援（中/英文） |
| 🔄   | 使用者自定義 Prompt 與模組參數 |
| 🔄   | 多模型選擇支援（Claude、Gemini 等） |
| 🔄   | 語音輸入模組（Whisper、Deepgram 研究中） |
| 🔄   | 匯出整合至 Notion / GitHub / Cursor（API 整合中） |
| 🔄   | 任務追蹤與甘特圖視覺化呈現 |

## 六、API 規格（規劃中）

| Endpoint              | 方法 | 功能說明 |
|-----------------------|------|-----------|
| /generate/prd         | POST | 產出產品需求文檔 |
| /generate/research    | POST | 市場調研與競品分析 |
| /generate/tasks       | POST | 任務拆解與排程建議 |
| /generate/kpis        | POST | KPI 與評估方式生成 |
| /export               | POST | 結果導出至外部系統（GitHub、Notion、Cursor） |

## 七、執行環境與安裝方式

- **必要條件**：
  - Python 3.10+
  - 安裝 OpenRouter API Key（.env）

- **安裝方式**：
```bash
pip install -r requirements.txt
```

## 八、補充說明

- 所有產出儲存於 `outputs/`，自動依時間命名
- Prompt 模板可於 `src/utils/prompts.py` 調整
- 控制流程定義於 `src/controller.py`
- 專案使用 Poetry 進行版本控管與開發管理

📎 範例結果與畫面請見 `docs/demo_screenshots/`

---

> ⚠️ 本產品仍為 MVP 版本，部分功能仍在開發中，若有合作或建議歡迎聯繫開發者團隊。