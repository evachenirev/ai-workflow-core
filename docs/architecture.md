# 系統架構說明

## 簡介
ai-workflow-core 是一套模組化 AI 多代理系統，目標是將使用者的非結構化想法轉化為可執行的計劃文件，並輔助產品開發流程的自動化。

## 架構圖
```mermaid
flowchart TD
  UI[使用者輸入 (Streamlit UI)]
  Controller[Workflow Controller\n(流程調度與代理管理)]
  
  subgraph Agents[AI Agents 多代理]
    PRD[PRD Agent\n(prd_agent.py)]
    Research[Research Agent\n(research_agent.py)]
    Task[Task Agent\n(task_agent.py)]
    KPI[KPI Agent\n(kpi_agent.py)]
  end

  OutputGen[輸出產生器\n(helpers.py)]
  OutputFile[Markdown 輸出檔案\n(outputs/)]

  UI --> Controller
  Controller --> PRD
  Controller --> Research
  Controller --> Task
  Controller --> KPI

  PRD --> OutputGen
  Research --> OutputGen
  Task --> OutputGen
  KPI --> OutputGen

  OutputGen --> OutputFile


## 模組說明

- **main.py**：Streamlit 前端介面，負責與使用者互動並顯示結果。
- **controller.py**：負責接收輸入、呼叫不同 Agent 並管理流程。
- **agents/**：包含四個專責的 AI Agent，分別處理 PRD 撰寫、市場調研、任務分解與 KPI 設定。
- **utils/prompts.py**：存放各 Agent 的 Prompt 模板。
- **utils/helpers.py**：共用輔助函式，例如文件輸出、日期處理等。
- **outputs/**：自動產生的 Markdown 文件存放目錄。
- **docs/**：說明文件、架構圖及 Demo 截圖。

## 技術細節

- **多代理架構**：使用獨立 Agent 模組化設計，方便擴展與測試。
- **AI 模型接入**：靈活支援 GPT-4、Claude、Gemini 等多種大模型。
- **UI 技術**：採用 Streamlit 快速搭建互動介面。
- **文件輸出**：自動產生可直接使用的 Markdown 格式報告。
- **擴展性**：後續可加入 Notion、VSCode API 整合。
