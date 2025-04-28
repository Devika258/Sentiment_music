from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.services.openai_service import analyze_sentiment
from app.services.auth_service import get_current_user
from app.services.spotify_service import search_tracks_by_mood  # ✅ Spotify integration
from datetime import datetime
from typing import List, Dict, Any
import traceback

# Router instance
router = APIRouter()

# In-memory history per user
user_history: Dict[str, List[Dict[str, Any]]] = {}

# Request Models
class MoodInput(BaseModel):
    text: str

class MoodOnly(BaseModel):
    mood: str

# Route 1: Classify mood using OpenAI
@router.post("/classify-mood", summary="Classify User Mood", tags=["Mood Analysis"])
async def classify_user_mood(input: MoodInput):
    """
    Uses OpenAI to classify the user's text into one of the predefined moods.
    """
    try:
        mood = await analyze_sentiment(input.text)
        return {"mood": mood}
    except Exception as e:
        print("❌ classify_user_mood error:")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail="OpenAI classification failed.")

# Route 2: Get a playlist from Spotify and log the access
@router.post("/playlist", summary="Get Playlist", tags=["Mood Analysis"])
def get_playlist(
    mood_input: MoodOnly,
    current_user: dict = Depends(get_current_user)
):
    """
    Returns a Spotify-based playlist based on the specified mood and deducts one credit.
    """
    mood = mood_input.mood.lower()

    if current_user["credits"] <= 0:
        raise HTTPException(status_code=403, detail="Out of credits. Please upgrade your plan.")

    playlist = search_tracks_by_mood(mood)  # 🎧 Use Spotify search
    if not playlist:
        raise HTTPException(status_code=404, detail="No playlist found for this mood.")

    current_user["credits"] -= 1  # 💳 Deduct credit

    # Save the entry
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "mood": mood,
        "playlist": playlist
    }
    user_history.setdefault(current_user["username"], []).append(entry)

    return {
        "user": current_user["username"],
        "mood": mood,
        "playlist": playlist,
        "remaining_credits": current_user["credits"]
    }

# Route 3: Return playlist history for current user
@router.get("/history", summary="View Playlist History", tags=["Mood Analysis"], response_model=Dict[str, Any])
def get_user_history(current_user: dict = Depends(get_current_user)):
    """
    Returns the authenticated user's mood-based playlist generation history.
    """
    return {
        "user": current_user["username"],
        "history": user_history.get(current_user["username"], [])
    }
