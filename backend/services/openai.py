import os
import openai
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Set your OpenAI key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Check for API key at startup
if not openai.api_key:
    raise ValueError("❌ OPENAI_API_KEY is not set. Please check your .env file or environment variables.")

# Define valid moods for classification
VALID_MOODS = {
    "happy",
    "sad",
    "energetic",
    "relaxed",
    "romantic",
    "angry",
    "nostalgic"
}

def classify_mood(text: str) -> str:
    """
    Classifies the given text into a mood using OpenAI's ChatCompletion.

    Returns a valid mood from the predefined list.
    Falls back to 'relaxed' if classification fails or returns an invalid response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Classify the user's message into one of the following moods: "
                        "happy, sad, energetic, relaxed, romantic, angry, nostalgic. "
                        "Reply with just one word from that list. Do not explain."
                    )
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        # Safely extract content
        mood = response.choices[0].message.get("content", "").strip().lower()
        print(f"[DEBUG] OpenAI returned mood: '{mood}'")

        if mood in VALID_MOODS:
            return mood
        else:
            print(f"[WARNING] OpenAI returned invalid mood: '{mood}', defaulting to 'relaxed'")
            return "relaxed"

    except Exception as e:
        print("[ERROR] classify_mood failed:", str(e))
        return "relaxed"
