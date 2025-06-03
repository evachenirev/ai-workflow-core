"""
prd_agent.py
負責生成產品需求文件 (PRD)
"""

class PRDAgent:
    def __init__(self):
        # 初始化 AI 模型與參數
        pass

    def generate_prd(self, user_input: str, research_report: str) -> str:
        # TODO: 呼叫 LLM，組合 prompt 並取得 PRD Markdown 內容
        prd_content = f"# 產品需求文件\n\n基於輸入: {user_input}\n\n調研結果摘要:\n{research_report}\n\n..."
        return prd_content
