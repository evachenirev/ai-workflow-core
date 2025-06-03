from utils.llm import OpenRouterClient

class KPIAgent:
    def __init__(self, llm_client=None):
        self.llm = llm_client or OpenRouterClient()

    def generate_kpi(self, idea_text):
        prompt = (
            f"請針對以下產品想法提出關鍵績效指標 (KPI):\n"
            f"{idea_text}\n"
            f"請列出可衡量產品成功的指標。"
        )
        result = self.llm.chat(prompt)
        return result
