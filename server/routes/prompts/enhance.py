from fastapi import APIRouter, HTTPException, Depends
from .schemas import PromptInput, PromptEnhanced
from routes.auth.token import get_current_user
from transformers import pipeline

router = APIRouter()

try:
    enhancer = pipeline("text2text-generation", model="google/flan-t5-small")
except Exception as e:
    enhancer = None
    enhancer_load_error = str(e)
else:
    enhancer_load_error = None

@router.post("/enhance", response_model=PromptEnhanced)
def enhance_prompt(prompt_input: PromptInput, current_user=Depends(get_current_user)):
    """
    Enhance the prompt using a transformer-based model for clarity, grammar, and completeness.
    """
    text = prompt_input.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")
    if enhancer is None:
        raise HTTPException(status_code=500, detail=f"Enhancer model could not be loaded: {enhancer_load_error}")
    try:
        hf_input = (
            "Rewrite the prompt to be clearer and more specific for code generation.\n\n"
            "Example:\n"
            "Original: create a function to add two numbers\n"
            "Improved: Write a Python function named add_numbers that takes two integers as input and returns their sum.\n\n"
            f"Original: {text}\nImproved:"
        )
        response = enhancer(hf_input, max_length=64)
        enhanced = response[0]['generated_text'].strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Enhancement failed: {str(e)}")
    return PromptEnhanced(original=text, enhanced=enhanced)
