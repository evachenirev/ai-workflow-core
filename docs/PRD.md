# AI Workflow Core 中文產品規格書（PRD）

## 一、產品定位與目標

**AI Workflow Core** 是一套由多代理人（Multi-Agent）驅動的智慧工作流程平台，
協助使用者將非結構化的初步想法（文字或語音），自動轉化為具結構性的產品文件、技術規劃、KPI 指標與任務拆解。
系統亦支援整合如 Cursor、Notion、GitHub 等工具，實現產品開發流程的自動化與持續追蹤。

### 🎯 主要目標客群

* 🚀 初創團隊與產品經理：快速構思產品原型與文件化
* 🧑‍💻 自由開發者：從想法快速落地執行
* 🏢 中小企業：協助流程自動化與任務規劃

## 二、功能模組總覽

| 模組         | 功能說明                                    |
| ---------- | --------------------------------------- |
| 💡 想法輸入    | 以文字或語音輸入原始構想，支援多語系（中/英）                 |
| 📄 PRD 產生器 | 由 PRD Agent 將輸入轉換為產品需求文件（PRD）           |
| 📊 市場研究器   | 利用 Research Agent 回傳競品、目標市場、Persona 等資料 |
| ✅ 任務分解器    | Task Agent 產生可執行任務、優先順序與排程建議            |
| 🎯 KPI 推導器 | KPI Agent 自動產出可衡量的關鍵指標與評估方法             |
| 📂 輸出管理    | 所有輸出皆以 Markdown 儲存，可導出至外部系統或 Git Repo   |

## 三、使用流程（User Flow）

1. 使用者透過 Streamlit 前端輸入想法（例如：「我想開發一個幫助小型店家管理庫存的 App」）
2. Controller 組件接收輸入，分派給對應的 AI Agent 處理
3. 各 Agent 串接 GPT-4 / Claude 等 LLM API 進行任務推論
4. 統整所有產出內容：PRD、競品分析、任務列表、KPI、預估時程
5. 使用者可編輯並選擇匯出：Notion / GitHub / Cursor

## 四、技術架構（概要）

📄 架構圖請參見 `docs/architecture.md`

### 核心組件

* **前端介面**：基於 Streamlit 開發，提供語音/文字輸入與輸出展示
* **LangChain**：用於多代理人調度與工作流程控制
* **多模型支援**：可搭配 GPT-4、Claude、Gemini 等主流 LLM API
* **快取策略**：支援 SQLite 本地快取或 Redis 記憶體型快取
* **模組化結構**：原始碼分為 `src/agents`, `src/utils`, `outputs/` 等目錄

## 五、產品路線與規劃

| 狀態 | 功能項目                           |
| -- | ------------------------------ |
| ✅  | 多語介面支援（目前支援中/英文）               |
| 🔄 | 團隊協作模式（多人共享輸出文件）               |
| 🔄 | 使用者自定義 Prompt 模板（個性化 Agent 任務） |
| 🔄 | 自動推播任務追蹤與時程提醒                  |

## 六、API 規格（選用）

| API Endpoint         | 方法   | 說明                              |
| -------------------- | ---- | ------------------------------- |
| `/generate/prd`      | POST | 根據輸入產生產品需求文件 PRD                |
| `/generate/research` | POST | 產生市場調查與競品資料                     |
| `/generate/tasks`    | POST | 自動切分任務與建議時程                     |
| `/generate/kpis`     | POST | 推導關鍵績效指標                        |
| `/export`            | POST | 將結果同步至 GitHub / Notion / Cursor |

## 七、依賴與執行環境

* 必要 API Key：

  * OpenAI（GPT-4）
  * Anthropic（Claude）

* 建議執行環境：

  * Python 3.10 以上
  * 使用虛擬環境管理（如 `venv`）

### 安裝方式

```bash
pip install -r requirements.txt
```

## 八、補充說明

* 所有產出文件皆儲存於 `outputs/` 資料夾，並自動依時間命名
* 可自定 Agent Prompt：修改 `src/utils/prompts.py`
* 可調整調度流程：編輯 `src/controller.py`

📎 附註：

* 若需 Demo 或影片介紹，請見 `docs/demo_screenshots/`
* 此 PRD 為 MVP 初版，後續版本將持續優化交互體驗與輸出格式
