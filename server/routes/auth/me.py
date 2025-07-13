from fastapi import APIRouter, Depends
from database.database import get_db
from sqlalchemy.orm import Session
from .token import get_current_user

router = APIRouter()

@router.get("/me")
def get_me(current_user = Depends(get_current_user)):
    return current_user
