from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ...database import get_db

router = APIRouter()

class SignupInput(BaseModel):
    email: str
    password: str

@router.post("/signup")
def signup(signup_input: SignupInput, db: Session = Depends(get_db)):
    # Dummy logic: Replace with real user creation logic
    existing_user = db.query(User).filter(User.email == signup_input.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    # Add user creation logic here
    return {"msg": "User created successfully"}
