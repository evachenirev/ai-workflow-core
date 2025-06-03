from utils.llm import OpenRouterClient

class PRDAgent:
    def __init__(self, llm_client=None):
        self.llm = llm_client or OpenRouterClient()

    def generate_prd(self, idea_text):
        prompt = (
            f"請根據以下產品想法撰寫一份詳細的產品需求文件 (PRD):\n"
            f"{idea_text}\n"
            f"請包含目標、功能、使用者需求和預期效益，"
            f"用條列式清楚表達。"
        )
        result = self.llm.chat(prompt)
        return result
