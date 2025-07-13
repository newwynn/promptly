from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database.database import get_db
from .token import create_access_token

router = APIRouter()

class LoginInput(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(login_input: LoginInput, db: Session = Depends(get_db)):
    # Dummy logic: Replace with real user verification
    user = db.query(User).filter(User.email == login_input.email).first()
    if not user or not user.verify_password(login_input.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
