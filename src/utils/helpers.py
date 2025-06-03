"""
helpers.py
共用輔助函式，例如文件儲存、時間格式轉換等
"""

import os
from datetime import datetime

OUTPUT_DIR = "outputs"

def save_markdown(filename_prefix: str, content: str) -> str:
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(OUTPUT_DIR, f"{filename_prefix}_{timestamp}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath
