from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import User
from routes.auth.token import create_access_token

router = APIRouter()

class SignupInput(BaseModel):
    email: str
    password: str

@router.post("/signup")
def signup(signup_input: SignupInput, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == signup_input.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    # Add user creation logic here
    user = User(email=signup_input.email, password=User.get_password_hash(signup_input.password))
    db.add(user)
    db.commit()

    access_token = create_access_token({"sub": user.email})
    return {
        "message": "User created successfully",
        "access_token": access_token, 
        "token_type": "bearer",
    }
