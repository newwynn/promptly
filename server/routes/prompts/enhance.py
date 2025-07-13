from fastapi import APIRouter, HTTPException, Depends
from .schemas import PromptInput, PromptEnhanced
from ...auth.token import get_current_user

router = APIRouter()

@router.post("/enhance", response_model=PromptEnhanced)
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
