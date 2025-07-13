from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from routes import auth, prompts
from middleware import LoggingMiddleware
from database.database import engine, get_db
import database.models as models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(LoggingMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(prompts.router, prefix="/api/v1")

@app.get("/", response_class=PlainTextResponse)
def read_root():
    return "Welcome to Promptly API - The Prompt Management System"

@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    try:
        from sqlalchemy import text
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database connection error: {str(e)}"
        )