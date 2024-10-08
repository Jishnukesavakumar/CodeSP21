from typing import List
from pydantic import BaseModel

class OpenAIMessage(BaseModel):
    role: str
    content: str

class OpenAIRequest(BaseModel):
    messages: List[OpenAIMessage]
    