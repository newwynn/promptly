from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=50)
    full_name: Optional[str] = Field(None, max_length=100)

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate):
    return {
        "message": "User created successfully",
        "email": user.email,
        "full_name": user.full_name
    }
