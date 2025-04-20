import pytest
import requests

BASE_URL = "http://localhost:8000"

@pytest.fixture(scope="module")
def user_token():
    # Register
    requests.post(f"{BASE_URL}/auth/register", json={"username": "testuser", "password": "testpass"})
    # Login
    response = requests.post(f"{BASE_URL}/auth/login", data={"username": "testuser", "password": "testpass"})
    token = response.json()["access_token"]
    return token

def test_root():
    res = requests.get(f"{BASE_URL}/")
    assert res.status_code == 200
    assert "message" in res.json()

def test_classify_mood():
    data = {"text": "I feel relaxed and calm."}
    res = requests.post(f"{BASE_URL}/api/mood/classify-mood", json=data)
    assert res.status_code == 200
    assert "mood" in res.json()

def test_get_playlist(user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    data = {"mood": "relaxed"}
    res = requests.post(f"{BASE_URL}/api/mood/playlist", json=data, headers=headers)
    assert res.status_code == 200
    json_data = res.json()
    assert "playlist" in json_data
    assert isinstance(json_data["playlist"], list)

def test_get_history(user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    res = requests.get(f"{BASE_URL}/api/mood/history", headers=headers)
    assert res.status_code == 200
    json_data = res.json()
    assert "history" in json_data