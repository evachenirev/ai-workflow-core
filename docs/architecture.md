# 系統架構說明

## 簡介
ai-workflow-core 是一套模組化 AI 多代理系統，目標是將使用者的非結構化想法轉化為可執行的計劃文件，並輔助產品開發流程的自動化。

## 架構圖
```mermaid
flowchart TD
  UI["使用者輸入 (Streamlit UI)"]
  Controller["Workflow Controller\n(流程調度與代理管理)"]
  
  subgraph Agents["AI Agents 多代理"]
    PRD["PRD Agent\n(prd_agent.py)"]
    Research["Research Agent\n(research_agent.py)"]
    Task["Task Agent\n(task_agent.py)"]
    KPI["KPI Agent\n(kpi_agent.py)"]
  end

  OutputGen["輸出產生器\n(helpers.py)"]
  OutputFile["Markdown 輸出檔案\n(outputs/)"]

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
