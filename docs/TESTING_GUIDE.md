# 🧪 AI Workflow Core 專案測試指南─Testing Guide

> 本文件為 AI Workflow Core 專案的獨立測試指南，詳細說明測試前準備、專項架構、功能驗證流程、單元測試方法，以及錯誤排除指彌。

---

## 📌 一、測試前準備

### 1. 安裝 Poetry 並建立處空環境

```bash
# 安裝 Poetry（若尚未安裝）
curl -sSL https://install.python-poetry.org | python3 -

# 安裝專案依賴
poetry install
```

### 2. 起始 Poetry 專案

```bash
poetry init --no-interaction
```

### 3. 安裝必要套件

```bash
poetry add streamlit openai python-dotenv pytest
```

### 4. 啟動處空環境

```bash
poetry shell
```

### 5. 環境需求

* Python >= 3.10
* Streamlit >= 1.30
* OpenAI / Anthropic API Key 已設定（放置於 `.env`）

## 🧧 二、專案架構概覽

```
├── .github/
│   └── workflows/
│       └── test.yml                # CI/CD 自動化測試流程
├── src/
│   ├── main.py                    # Streamlit 入口點
│   ├── agents/                    # 各任務代理人模組
│   │   ├── prd_agent.py
│   │   ├── research_agent.py
│   │   ├── task_agent.py
│   │   └── kpi_agent.py
│   └── utils/                     # Prompt 與工具函式
│       ├── prompts.py
│       └── helpers.py
├── tests/
│   └── test_controller.py         # 控制流程單元測試
├── .streamlit/config.toml         # Streamlit UI 設定檔
├── requirements.txt               # 備用安裝清單
├── README.md
├── docs/
    ├── PRD.md
    ├── architecture.md
    ├── TESTING_GUIDE.md           # 本文件
    └── demo_screenshots/
```

## 🧺 三、測試項目列表與完成狀態

| 模組                 | 測試項目            | 檢核點                        | 是否完成 |
| ------------------ | --------------- | -------------------------- | ---- |
| main.py            | Streamlit UI 啟動 | 本機頁面可正常操作                  | ✅    |
| Controller         | 正確分配至各 Agent    | 無錯誤，輸出符合預期                 | ✅    |
| prd\_agent.py      | PRD 欄位完整且語意通順   | 包含 Title、Problem、Scope 等欄位 | ⬜    |
| research\_agent.py | 回傳有效市場調查內容      | 至少包含競品兩項及 Persona          | ⬜    |
| task\_agent.py     | 任務合理分配與排序       | 含優先級、Deadline 建議           | ⬜    |
| kpi\_agent.py      | KPI 格式正確且可測量    | 含指標與評估方法                   | ⬜    |
| 輸出檔案               | Markdown 正確輸出   | outputs/ 目錄有正確檔案生成         | ⬜    |

## 🤩 四、功能測試流程

1. 啟動 App 並輸入測試語句：

```bash
streamlit run src/main.py
```

2. 範例輸入：

* 中文示範：`我想開發一個幫助街邊早餐店管理庫存的 App`
* 英文示範：`Build a mobile app to help small bakeries track inventory and alert low stock`

3. 驗證各 Agent 輸出內容：

| Agent    | 預期輸出欄位                                |
| -------- | ------------------------------------- |
| PRD      | Title, Problem, Target User, Features |
| Research | Persona, Competitors, Market Need     |
| Task     | 執行項目、優先順序、Deadline 建議                 |
| KPI      | 數值型 KPI、測量方法                          |

4. 檢查輸出 Markdown 檔案：

```
outputs/YYYY-MM-DD/prd.md
outputs/YYYY-MM-DD/tasks.md
outputs/YYYY-MM-DD/kpi.md
```

確認檔案結構正確，標題、段落合理

## 🧠 五、單元測試─Unit Test

執行：

```bash
pytest tests/test_controller.py -v
```

範例測試程式碼：

```python
def test_process_input():
    controller = WorkflowController()
    user_text = "設計一款智能助理App"
    files = controller.process_input(user_text)
    assert len(files) == 4
    for f in files:
        assert f.endswith(".md")
```

## 🧰 六、除錯與調整指卜

* 修改 Agent Prompt：`src/utils/prompts.py`
* 調整任務流程邏輯：`src/controller.py`
* API Key 設定問題：確認 `.env` 檔案是否已正確配置
* Streamlit 啟動問題：檢查 `.streamlit/config.toml` 設定

## ✅ 七、完成驗證標準

* 所有 Agent 輸出包含有效且完整資訊
* Markdown 檔案輸出無錯誤
* 單元測試皆通過
* Streamlit App 可穩定啟動與操作

## 📌 附註

* 本指南為 PoC 版本測試指彌，未來版本將補充壓力測試與效能評估
* 建議將測試流程入化 GitHub Actions 或其他 CI/CD 工具，自動化驗證

📉 作者：AI Workflow Core 開發者
🗓️ 更新日期：2025-06-03
🔗 文件類型：測試指彌─Testing Guide
