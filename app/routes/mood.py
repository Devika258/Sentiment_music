from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.openai_service import analyze_sentiment

router = APIRouter()

# ✅ Mock playlist data
MOCK_PLAYLISTS = {
    "happy": ["Good Vibes Only", "Sunshine Anthem", "Smile With Me"],
    "sad": ["Rainy Day Blues", "Melancholy Mood", "Alone Again"],
    "relaxed": ["Chillout Lounge", "Coffeehouse Jazz", "Ocean Sounds"],
    "energetic": ["Workout Mix", "Hype Beats", "Run Wild"],
    "angry": ["Hard Rock Hits", "Metal Madness", "Rage Mode"],
    "romantic": ["Love Ballads", "Candlelight Classics", "Heartbeats"],
    "focused": ["Deep Work Vibes", "Productivity Flow", "Lo-Fi Study"],
    "melancholic": ["Soft Strings", "Memory Lane", "Sad Symphony"]
}

# 📥 Input model for mood classification
class MoodInput(BaseModel):
    text: str

# 📥 Input model for playlist retrieval
class MoodOnly(BaseModel):
    mood: str

# 🔍 Route 1: Classify mood using OpenAI
@router.post("/classify-mood")
async def classify_user_mood(input: MoodInput):
    try:
        mood = await analyze_sentiment(input.text)
        return {"mood": mood}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error classifying mood: {e}")

# 🎵 Route 2: Return playlist for given mood
@router.post("/playlist")
async def get_playlist(mood_input: MoodOnly):
    mood = mood_input.mood.lower()
    playlist = MOCK_PLAYLISTS.get(mood)
    if playlist:
        return {"mood": mood, "playlist": playlist}
    else:
        raise HTTPException(status_code=404, detail="Mood not recognized")
