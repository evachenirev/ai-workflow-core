# 🧪 AI Workflow Core 專案測試指南（Testing Guide）

> 本文件為 AI Workflow Core 專案的獨立測試指引，涵蓋環境建置、功能驗證、Agent 行為確認及流程測試。

---

## 📌 一、測試前準備

### 1. 安裝 Poetry 並建立虛擬環境

```bash
# 安裝 Poetry（若尚未安裝）
curl -sSL https://install.python-poetry.org | python3 -

# 建立虛擬環境並安裝依賴
poetry install

# 若尚未建立 pyproject.toml，請先執行
poetry init --no-interaction

# 安裝必要套件
poetry add streamlit openai python-dotenv pytest

# 啟動虛擬環境
poetry shell
2. 環境需求
Python >= 3.10

Streamlit >= 1.30

OpenAI / Anthropic API Key 已設定於 .env

🧷 二、專案架構概覽
bash
複製
編輯
├── .github/
│   └── workflows/
│       └── test.yml
├── src/
│   ├── main.py                 # Streamlit 入口點
│   ├── agents/                 # 各任務代理人
│   │   ├── prd_agent.py
│   │   ├── research_agent.py
│   │   ├── task_agent.py
│   │   └── kpi_agent.py
│   └── utils/                 # Prompt 與工具函式
│       ├── prompts.py
│       └── helpers.py
├── tests/
│   └── test_controller.py     # 控制流程測試
├── .streamlit/config.toml     # Streamlit UI 設定
├── requirements.txt           # 備用安裝列表
├── README.md
├── docs/
│   ├── PRD.md
│   ├── architecture.md
│   ├── TESTING_GUIDE.md
│   └── demo_screenshots/
🧪 三、測試項目列表
模組	測試項目	檢核點	是否完成
主程式 main.py	Streamlit UI 啟動	localhost 頁面正常可操作	✅
Controller	Agent 分派邏輯	日誌無錯誤、輸出結果正確	✅
prd_agent.py	PRD 欄位完整度	title / problem / scope 等存在	⬜
research_agent.py	有效回傳市場調查內容	至少包含 Persona、競品2項	⬜
task_agent.py	任務分類與數量合理	包含優先級與時程建議	⬜
kpi_agent.py	KPI 格式及衡量性	指標 + 評估方法	⬜
輸出儲存	Markdown 檔案生成	outputs/ 目錄正確生成檔案	⬜

🧩 四、功能測試流程
啟動 App：

bash
複製
編輯
streamlit run src/main.py
輸入測試語句：

中文範例：

複製
編輯
我想開發一個幫助街邊早餐店管理庫存的 App
英文範例：

css
複製
編輯
Build a mobile app to help small bakeries track inventory and alert low stock
驗證各 Agent 輸出內容：

Agent	預期內容說明
PRD Agent	Title, Problem, Target User, Features
Research Agent	Persona, Competitors, Market Need
Task Agent	執行項目、優先順序、Deadline 建議
KPI Agent	數值型 KPI、測量方法

檢查輸出結果：

檔案路徑範例：

bash
複製
編輯
outputs/YYYY-MM-DD/prd.md
outputs/YYYY-MM-DD/tasks.md
確認 Markdown 結構及標題段落合理。

🧠 五、單元測試（Unit Test）
執行單元測試指令：

bash
複製
編輯
pytest tests/test_controller.py -v
範例測試邏輯：

python
複製
編輯
def test_controller_dispatch():
    input_text = "開發一個協助自由接案者的時間管理 App"
    result = controller.process(input_text)
    assert "PRD" in result
    assert "tasks" in result
🧰 六、除錯與調整
Agent Prompt 位於 src/utils/prompts.py，可自由編輯調整。

任務流程可修改 src/controller.py。

若遇 API Key 錯誤，請確認 .env 是否正確設定。

✅ 七、完成驗證標準
所有 Agent 輸出皆含有效資訊。

Markdown 輸出檔案無錯誤並格式正確。

單元測試全數通過。

Streamlit App 可穩定啟動與操作。

📎 附註
本測試指南為 PoC 版本，未來可補充壓力測試與效能評估。

CI/CD 自動化測試可導入 GitHub Actions。

📌 作者：AI Workflow Core 開發者
📅 更新時間：2025-06-03
🔗 文件類型：測試指引（Testing Guide）