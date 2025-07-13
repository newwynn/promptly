from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict
from scoring import analyze_prompt
from routes.auth import get_current_user

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

class PromptEnhanced(BaseModel):
    original: str
    enhanced: str

@router.post("/prompts/get-score", response_model=PromptScore)
def get_prompt_score(prompt_input: PromptInput, current_user=Depends(get_current_user)):
    """
    Analyze the prompt and return a detailed score breakdown.
    """
    if not prompt_input.text.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")
    return analyze_prompt(prompt_input.text)

@router.post("/prompts/enhance", response_model=PromptEnhanced)
def enhance_prompt(prompt_input: PromptInput, current_user=Depends(get_current_user)):
    """
    Enhance the prompt for clarity, grammar, and completeness.
    """
    text = prompt_input.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")
    enhanced = text[0].upper() + text[1:].strip()
    if not enhanced.endswith(('.', '!', '?')):
        enhanced += '.'
    enhanced = ' '.join(enhanced.split())
    return PromptEnhanced(original=text, enhanced=enhanced)
