from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from database.database import get_db
from database.models import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=50)
    full_name: Optional[str] = Field(None, max_length=100)

class UserResponse(BaseModel):
    email: str
    full_name: Optional[str] = None

    class Config:
        from_attributes = True

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Hash the password
    hashed_password = User.get_password_hash(user.password)
    
    # Create new user
    db_user = User(
        email=user.email,
        password=hashed_password,
        full_name=user.full_name
    )
    
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error creating user"
        )
    
    return db_user
