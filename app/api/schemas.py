from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserCreate(UserBase):
    password: str


class UserInDB(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True


class User(UserInDB):
    pass


# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


# Credit schemas
class CreditBase(BaseModel):
    amount: int


class CreditCreate(CreditBase):
    user_id: int


class Credit(CreditBase):
    id: int
    user_id: int
    last_updated: datetime

    class Config:
        orm_mode = True


# Recommendation schemas
class RecommendationBase(BaseModel):
    sentiment: str


class RecommendationCreate(RecommendationBase):
    user_id: int


class Recommendation(RecommendationBase):
    id: int
    user_id: int
    spotify_playlist_id: str
    created_at: datetime

    class Config:
        orm_mode = True


# Sentiment request schema
class SentimentRequest(BaseModel):
    text: str