import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# 🔐 Load environment variables from .env
load_dotenv()

# 🔑 Credentials from .env file
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# 🧠 Spotify auth setup
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

# 🎯 Map moods to search keywords (can be expanded)
MOOD_KEYWORDS = {
    "happy": "feel good",
    "sad": "melancholy acoustic",
    "relaxed": "chill vibes",
    "energetic": "workout motivation",
    "romantic": "romantic slow",
    "angry": "heavy metal",
    "focused": "deep focus",
    "melancholic": "piano ambient"
}

# 🔍 Search tracks by mood keyword
def search_tracks_by_mood(mood: str, limit: int = 5):
    keyword = MOOD_KEYWORDS.get(mood.lower(), mood)
    results = spotify.search(q=keyword, type="track", limit=limit)

    tracks = results.get("tracks", {}).get("items", [])
    if not tracks:
        return []

    return [f"{track['name']} - {track['artists'][0]['name']}" for track in tracks]
