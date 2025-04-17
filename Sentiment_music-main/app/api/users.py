from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User, Credit
from app.api.schemas import User as UserSchema, Credit as CreditSchema
from app.auth.jwt import get_current_active_user

router = APIRouter()

@router.get("/me", response_model=UserSchema)
def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@router.get("/credits", response_model=CreditSchema)
def get_user_credits(current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    credits = db.query(Credit).filter(Credit.user_id == current_user.id).first()
    if not credits:
        raise HTTPException(status_code=404, detail="Credits not found")
    return credits