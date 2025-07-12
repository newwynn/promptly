from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import logging
import traceback

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
    try:
        print(f"Received signup request for email: {user.email}")
        
        # Check if user already exists
        db_user = db.query(User).filter(User.email == user.email).first()
        if db_user:
            print(f"User with email {user.email} already exists")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        print("Hashing password...")
        # Hash the password
        hashed_password = User.get_password_hash(user.password)
        print("Password hashed successfully")
        
        # Create new user
        db_user = User(
            email=user.email,
            password=hashed_password,
            full_name=user.full_name
        )
        
        print("Adding user to database...")
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        print(f"User created successfully with ID: {db_user.id}")
        
        return db_user
        
    except Exception as e:
        db.rollback()
        print(f"Error in signup: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        
        error_detail = str(e)
        if "UNIQUE constraint failed" in error_detail:
            error_detail = "Email already registered"
            
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=error_detail
        )
