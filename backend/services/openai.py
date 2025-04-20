import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

VALID_MOODS = {"happy", "sad", "energetic", "relaxed", "romantic", "angry", "nostalgic"}

def classify_mood(text: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a strict classifier. "
                        "Return only one word: happy, sad, energetic, relaxed, romantic, angry, or nostalgic. "
                        "Do not explain or add extra text. Just return the mood that best fits."
                    )
                },
                {
                    "role": "user",
                    "content": f"Classify this sentence: {text}"
                }
            ]
        )

        mood = response.choices[0].message["content"].strip().lower()
        print("[DEBUG] Mood received from OpenAI:", mood)
        return mood if mood in VALID_MOODS else "relaxed"

    except Exception as e:
        print("[ERROR] classify_mood exception:", e)
        return "relaxed"
