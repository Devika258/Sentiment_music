import asyncio
from typing import Dict

# Simulated queue (could be replaced with real one like Celery later)
mood_queue = []

async def process_queue_request(username: str, mood: str) -> Dict:
    """
    Simulate mood-based playlist processing with artificial delay.
    """
    print(f"🕐 Adding to queue: {username} wants playlist for mood: {mood}")
    mood_queue.append((username, mood))

    # Simulate processing time
    await asyncio.sleep(2)  # simulate queue delay

    print(f"✅ Processed request for {username}")
    mood_queue.remove((username, mood))

    return {
        "status": "processed",
        "username": username,
        "mood": mood,
        "message": f"Mood '{mood}' processed for {username} 🎧"
    }
