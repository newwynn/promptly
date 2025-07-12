from fastapi import APIRouter, HTTPException
from schemas.prompt import PromptInput, PromptOutput
from services.prompt_runner import run_prompt

router = APIRouter()

@router.post("/run", response_model=PromptOutput)
def run_model(data: PromptInput):
    try:
        result = run_prompt(data.text)
        return {"output": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
