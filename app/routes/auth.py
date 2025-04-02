from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.services.auth_service import (
    hash_password, verify_password, create_access_token, fake_users_db
)

router = APIRouter()

class UserRegister(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user: UserRegister):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed = hash_password(user.password)
    fake_users_db[user.username] = {
        "username": user.username,
        "hashed_password": hashed,
        "credits": 10  # Default credit
    }
    return {"message": "User registered successfully"}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    db_user = fake_users_db.get(username)
    if not db_user or not verify_password(password, db_user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}
