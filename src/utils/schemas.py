from typing import List, Dict
from pydantic import BaseModel

class PRDOutput(BaseModel):
    title: str
    description: str
    features: List[str]
    user_stories: List[str]
    notes: str
