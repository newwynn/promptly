from fastapi import APIRouter, HTTPException, Depends
from .schemas import PromptInput, PromptScore
from scoring import analyze_prompt
from ...auth.token import get_current_user

router = APIRouter()

@router.post("/get-score", response_model=PromptScore)
def get_prompt_score(prompt_input: PromptInput, current_user=Depends(get_current_user)):
    """
    Analyze the prompt and return a detailed score breakdown.
    """
    if not prompt_input.text.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")
    return analyze_prompt(prompt_input.text)
