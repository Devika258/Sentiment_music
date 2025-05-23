from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user import User as DBUser
from services.openai_service import analyze_sentiment
from services.spotify_service import search_tracks_by_mood
import threading
import time

router = APIRouter(prefix="/mood", tags=["mood"])

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

class MoodRequest(BaseModel):
    text: str

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Decode user from JWT token
def get_current_user(token: str = Header(...), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=403, detail="Invalid token")
        user = db.query(DBUser).filter(DBUser.username == username).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")

# Simulated background processing for mood detection and Spotify playlist fetch
def process_mood_job(user: DBUser, text: str, db: Session):
    try:
        print(f"Processing mood job for user {user.username}...")
        time.sleep(2)  # simulate queue delay
        mood = analyze_sentiment(text)
        playlist = search_tracks_by_mood(mood)
        user.credits -= 1
        db.commit()
        print(f"[Notification] Job complete for {user.username} | Mood: {mood} | Remaining Credits: {user.credits}")
        print(f"[Playlist] {playlist}")
    except Exception as e:
        print(f"[Notification] Job failed for {user.username}: {str(e)}")

# API endpoint to submit mood classification and playlist generation job
@router.post("/")
def mood_to_music(request: MoodRequest, current_user: DBUser = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.credits < 1:
        raise HTTPException(status_code=402, detail="Not enough credits")

    job_thread = threading.Thread(target=process_mood_job, args=(current_user, request.text, db))
    job_thread.start()

    return {
        "status": "Job submitted",
        "message": f"Processing mood for user {current_user.username}. You will be notified upon completion."
    }