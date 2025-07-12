from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict
from scoring import analyze_prompt

router = APIRouter(
    tags=["prompts"]
)

class PromptInput(BaseModel):
    text: str

class PromptScore(BaseModel):
    clarity: int
    relevance: int
    creativity: int
    grammar: int
    completeness: int
    total_score: int

@router.post("/prompts/get-score", response_model=PromptScore)
def get_prompt_score(prompt_input: PromptInput):
    """
    Analyze the prompt and return a detailed score breakdown.
    """
    if not prompt_input.text.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")
    return analyze_prompt(prompt_input.text)
