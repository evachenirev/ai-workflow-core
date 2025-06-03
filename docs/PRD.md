AI Workflow Core 中文產品規格書（PRD）

一、產品定位與目標

AI Workflow Core 是一款由多代理人（Multi-Agent）驅動的智慧工作流程平台，旨在協助使用者從原始想法（文字或語音）自動轉化為可執行的產品文件、技術規劃、KPI 指標與任務分解，並可整合開發工具（如 Cursor、Notion）進行持續追蹤與迭代。

目標客群包含：

初創團隊與產品經理（快速構思原型）

自由開發者（將想法快速落地）

中小企業（流程自動化與任務規劃）

二、功能模組

功能模組

說明

想法輸入

文字或語音輸入原始構想（支援多語）

PRD 產生器

利用 PRD agent 將想法轉化為產品需求文件（Product Requirement Document）

市場研究器

透過 Research agent 回傳相關競品、目標市場、使用者輪廓等

任務分解器

利用 Task agent 自動切分可執行任務、排定優先順序與建議時程

KPI 推導器

由 KPI agent 自動推導出可衡量之關鍵指標與評估方法

輸出管理

所有輸出以 Markdown 儲存，可匯出至外部系統或 Git Repo

三、使用流程（User Flow）

使用者開啟平台，輸入想法（如：「我想開發一個幫助小型店家管理庫存的App」）

Controller 組件接收輸入並轉交至各代理人（agent）

各 agent 串接 LLM API（如 GPT-4, Claude 3）完成特定任務

回傳並統整輸出：包含 PRD、競品分析、任務清單、KPI 與時程建議

使用者可編輯內容，或一鍵導出至 Notion / GitHub / Cursor

四、技術架構（概要）

請參考 docs/architecture.md，主要包含：

Streamlit UI 前端

LangChain agent 調度核心

多模型選擇支援（GPT-4 / Claude / Gemini）

輕量快取（SQLite / Redis）

模組化架構：src/agents, src/utils, outputs/

五、未來規劃

✅ 多語介面支援（目前支援中英）

⏳ 團隊協作模式（多人共享輸出文件）

⏳ 使用者自定義 Prompt 模板（微調 agent 任務）

⏳ 自動推播與任務追蹤提醒

六、API 需求（如需擴展）

API

方法

描述

/generate/prd

POST

根據 input 產生 PRD

/generate/research

POST

產生市場調查內容

/generate/tasks

POST

自動切分任務

/generate/kpis

POST

自動產生 KPI

/export

POST

將輸出同步到 GitHub / Notion

七、依賴與前置

必要 API KEY：OpenAI, Anthropic

建議作業環境：Python 3.10+，建議使用 venv

安裝指令：pip install -r requirements.txt

八、附註

所有輸出將儲存於 outputs/ 資料夾，自動依時間戳記命名

若需客製化 Agent Prompt，請至 src/utils/prompts.py 編輯

若需調整執行流程，請修改 src/controller.py 調用邏輯