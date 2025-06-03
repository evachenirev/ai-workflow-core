import os
import requests

class OpenRouterClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENROUTER_API_KEY")
        self.endpoint = "https://openrouter.ai/api/v1/chat/completions"
        if not self.api_key:
            raise ValueError("請設定 OPENROUTER_API_KEY 環境變數或傳入 api_key")

    def chat(self, prompt, model="gpt-4o-mini", temperature=0.7):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature
        }
        resp = requests.post(self.endpoint, json=payload, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]
