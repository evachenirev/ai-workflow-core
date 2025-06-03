"""
kpi_agent.py
負責 KPI 指標設定與進度排程建議
"""

class KPIAgent:
    def __init__(self):
        pass

    def generate_kpi(self, tasks_content: str) -> str:
        # TODO: 呼叫 LLM 產生 KPI 指標與 deadline 規劃
        return f"# KPI 指標與排程\n\n基於任務清單:\n{tasks_content}\n\n指標與時間表..."
