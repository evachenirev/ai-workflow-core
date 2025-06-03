# Thoughts to Action

A modular AI-powered assistant that transforms your raw ideas into structured, actionable workflows — including PRDs, technical plans, timelines, and KPIs — using a multi-agent architecture. Designed for product managers, developers, and creators who want to go from "thoughts" to execution quickly.

## 🚀 Features

* 🧠 **Multi-agent system**: Specialized agents for PRD generation, research, task breakdown, and KPI setting
* 🔄 **Multi-model support**: GPT-4, Claude, Gemini, and more via unified agent orchestration
* ⚡ **One-click output**: Generate complete project plans (Markdown files) based on a single input
* 🔗 **Future integrations**: Notion, VSCode (Cursor), GitHub Projects, etc.
* 🧰 **Modular structure**: Easy to extend and customize each agent’s prompt or logic

## 🧱 Tech Stack

* **Python 3.10+**
* **LangChain** for LLM coordination
* **Streamlit** as frontend UI
* **OpenAI / Anthropic SDKs**
* **Markdown** outputs (stored in `outputs/`)

## 📁 Project Structure

```
thoughts-to-action/
├── src/
│   ├── main.py                     # Streamlit 主程式入口
│   ├── controller.py               # 處理 input/output 與 agent 調度
│   ├── agents/
│   │   ├── prd_agent.py
│   │   ├── research_agent.py
│   │   ├── task_agent.py
│   │   └── kpi_agent.py
│   ├── utils/
│   │   ├── prompts.py              # 各 agent prompt 模板
│   │   └── helpers.py              # 共用函式（檔案處理等）
├── outputs/                        # 輸出 Markdown 檔（自動命名）
├── docs/
│   ├── PRD.md                      # 原型規格說明
│   ├── architecture.md             # 系統架構簡述
│   └── demo_screenshots/
│       ├── ui_demo.png
│       └── workflow_diagram.png
├── .env.example                    # API KEY 範例格式
├── .gitignore                     # 忽略 venv, __pycache__, .env 等
├── requirements.txt               # pip 套件清單
├── .streamlit/config.toml         # Streamlit 設定（UI樣式可自定）
└── README.md                      # 主說明文件
```

## 🧪 Running the App

1. 安裝依賴：

```bash
pip install -r requirements.txt
```

2. 設定 `.env`：複製 `.env.example` 並填入你的 API 金鑰。

3. 啟動應用程式：

```bash
streamlit run src/main.py
```

## 🧪 Testing

```bash
pytest tests/
```

## 🛣️ Roadmap

* [ ] 一鍵產出 Notion / GitHub Cards
* [ ] 支援語音輸入（Whisper）
* [ ] 多語系介面與模型調度

## 📜 License

MIT © 2025
