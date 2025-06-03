from utils.llm import OpenRouterClient

class TaskAgent:
    def __init__(self, llm_client=None):
        self.llm = llm_client or OpenRouterClient()

    def generate_tasks(self, idea_text):
        prompt = (
            f"請將以下產品想法拆解成可執行的任務清單:\n"
            f"{idea_text}\n"
            f"請以條列式呈現，每項任務簡短明確，方便後續執行。"
        )
        result = self.llm.chat(prompt)
        return result
