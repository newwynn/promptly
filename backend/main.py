from fastapi import FastAPI
from api.routes import prompts

app = FastAPI()

app.include_router(prompts.router, prefix="/prompts", tags=["prompts"])

@app.get("/")
def read_root():
    return {"message": "Welcome to API"}
