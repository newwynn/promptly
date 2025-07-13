from pydantic import BaseModel

class PromptInput(BaseModel):
    text: str

class PromptScore(BaseModel):
    clarity: int
    relevance: int
    creativity: int
    grammar: int
    completeness: int
    total_score: int

class PromptEnhanced(BaseModel):
    original: str
    enhanced: str
