from utils.llm import OpenRouterClient

class ResearchAgent:
    def __init__(self, llm_client=None):
        self.llm = llm_client or OpenRouterClient()

    def generate_research(self, idea_text):
        prompt = (
            f"請根據以下產品想法，撰寫一份市場調查與競品分析報告:\n"
            f"{idea_text}\n"
            f"請說明市場趨勢、競爭者優劣與潛在機會。"
        )
        result = self.llm.chat(prompt)
        return result
