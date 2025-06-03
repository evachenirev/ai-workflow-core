"""
task_agent.py
負責任務分解與工作清單產生
"""

class TaskAgent:
    def __init__(self):
        pass

    def generate_tasks(self, prd_content: str) -> str:
        # TODO: 呼叫 LLM 產生具體任務列表與時間排程
        return f"# 任務分解清單\n\n基於 PRD:\n{prd_content}\n\n任務列表..."
