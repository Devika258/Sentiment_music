import os
import requests

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

def get_spotify_token():
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={"grant_type": "client_credentials"},
        auth=(CLIENT_ID, CLIENT_SECRET)
    )
    if response.status_code != 200:
        raise Exception("Spotify Token Error: " + response.text)
    return response.json()["access_token"]

def get_playlist_for_mood(mood: str):
    token = get_spotify_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "q": mood,
        "type": "track",
        "limit": 5
    }
    response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
    if response.status_code != 200:
        raise Exception("Spotify Search Error: " + response.text)

    items = response.json().get("tracks", {}).get("items", [])
    return [
        {
            "name": item["name"],
            "artist": item["artists"][0]["name"],
            "url": item["external_urls"]["spotify"]
        }
        for item in items
    ]