import os
from dotenv import load_dotenv

load_dotenv()  # 讀取根目錄的 .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
