from pydantic import BaseModel

class PromptInput(BaseModel):
    text: str

class PromptOutput(BaseModel):
    output: str

