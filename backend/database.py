import os
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = os.getenv("sqlite:///./test.db", "postgresql://Devika_S_R:MySecurePass123!@sentiment-db.c7iiu0w6o6rl.eu-north-1.rds.amazonaws.com:5432/sentiment_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    credits = Column(Integer, default=10)
    history = relationship("History", back_populates="user")

# Mood history model
class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    mood = Column(String)
    playlist = Column(Text)
    user = relationship("User", back_populates="history")

# Create tables
def init_db():
    Base.metadata.create_all(bind=engine)