# 🧪 AI Workflow Core 專案測試指南（Testing Guide）

> 📁 文件用途：此為專案的 **獨立測試文件**，針對功能驗證、架構測試、Agent 行為確認等進行完整流程設計與說明。

---

## 📌 一、測試前準備

### ✅ 1. 安裝 Poetry 並建立虛擬環境

```bash
# 安裝 Poetry（若尚未安裝）
curl -sSL https://install.python-poetry.org | python3 -

# 建立虛擬環境並安裝依賴
poetry install
```

### ✅ 2. 啟動虛擬環境

```bash
poetry shell
```

### ✅ 3. 環境需求

* Python >= 3.10
* OpenAI / Anthropic API Key
* Streamlit >= 1.30

---

## 🧷 二、專案架構概覽（非 README）

```text
├── src/
│   ├── main.py                 # Streamlit 入口點
│   ├── agents/                # 各任務代理人
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
│   └── demo_screenshots/
```

---

## 🧪 三、測試項目列表

| 模組                 | 測試項目               | 檢核點                         | 是否完成 |
| ------------------ | ------------------ | --------------------------- | ---- |
| 主程式 main.py        | Streamlit UI 是否能啟動 | localhost 頁面可操作             | ✅    |
| Controller 分派邏輯    | 能正確調用對應 Agent      | log 無錯誤、輸出正確                | ✅    |
| prd\_agent.py      | PRD 欄位完整、語意通順      | title / problem / scope 等存在 | ⬜    |
| research\_agent.py | 有效回傳市場調查內容         | 至少含競品2項、Persona             | ⬜    |
| task\_agent.py     | 任務數量、分類合理          | 含優先級與時程建議                   | ⬜    |
| kpi\_agent.py      | KPI 格式正確、具衡量性      | 指標 + 評估方法                   | ⬜    |
| 輸出儲存               | Markdown 檔案正確輸出    | outputs/ 正確生成檔案             | ⬜    |

---

## 🧩 四、功能測試流程

### 1️⃣ 啟動 App 並輸入測試用語句：

```bash
streamlit run src/main.py
```

範例輸入（中）：

> "我想開發一個幫助街邊早餐店管理庫存的 App"

範例輸入（英）：

> "Build a mobile app to help small bakeries track inventory and alert low stock"

---

### 2️⃣ 驗證各 Agent 輸出：

* **PRD 應包含：** Title, Problem, Target User, Features
* **Research 應包含：** Persona, Competitors, Market Need
* **Task 應包含：** 執行項、優先順序、Deadline 建議
* **KPI 應包含：** 數值型 KPI, 測量方法

---

### 3️⃣ 檢查輸出結果

* `outputs/YYYY-MM-DD/prd.md`
* `outputs/YYYY-MM-DD/tasks.md` ...等
* 確認 Markdown 結構正確、標題段落合理

---

## 🧠 五、單元測試（Unit Test）

請先執行：

```bash
pytest tests/test_controller.py -v
```

範例測試邏輯：

```python
def test_controller_dispatch():
    input_text = "開發一個協助自由接案者的時間管理 App"
    result = controller.process(input_text)
    assert "PRD" in result
    assert "tasks" in result
```

---

## 🧰 六、除錯與調整

* Agent Prompt 可編輯 `src/utils/prompts.py`
* 任務流程可修改 `src/controller.py`
* 若報錯 API 金鑰，請確認 `.env` 是否設置

---

## ✅ 七、完成驗證標準

* [ ] 所有 Agent 輸出皆含有效資訊
* [ ] Markdown 輸出存檔無錯誤
* [ ] 單元測試通過
* [ ] Streamlit 可穩定使用

---

## 📎 附註

* 本測試文檔為 PoC 測試指引，未來版本請補充壓力測試、效能評估。
* 若需 CI/CD 整合測試流程，可導入 GitHub Actions。

---

📌 作者：AI Workflow Core 開發者
📅 更新時間：2025-06-03
🔗 文件類型：測試指引（Testing Guide）
