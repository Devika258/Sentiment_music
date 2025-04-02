import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Predefined moods
VALID_MOODS = ['happy', 'sad', 'energetic', 'relaxed', 'romantic', 'angry', 'focused', 'melancholic']

async def analyze_sentiment(text: str) -> str:
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": (
                    "You're a mood classifier. Read the input and return only one emotion: "
                    "happy, sad, energetic, relaxed, romantic, angry, focused, melancholic.")},
                {"role": "user", "content": text}
            ],
            max_tokens=10,
            temperature=0.3
        )
        mood = response.choices[0].message.content.strip().lower()

        if mood not in VALID_MOODS:
            return "happy"  # fallback
        return mood

    except Exception as e:
        print(f"❌ OpenAI error: {e}")
        return "happy"  # fallback on error
