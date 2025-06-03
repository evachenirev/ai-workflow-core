"""
prompts.py
存放各 Agent 的 Prompt 模板
"""

PRD_PROMPT_TEMPLATE = """
請根據以下用戶輸入與調研結果，撰寫完整且具體的產品需求文件 (PRD)：

用戶輸入：
{user_input}

調研結果：
{research_report}

請包含功能描述、目標用戶、市場定位、技術需求等內容。
"""

# 其他 Agent 也可定義對應模板
