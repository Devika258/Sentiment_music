import openai
from app.config import settings

openai.api_key = settings.OPENAI_API_KEY

async def analyze_sentiment(text: str) -> str:
    """
    Analyze the sentiment of the provided text using OpenAI API.
    Returns a sentiment label that can be used to find appropriate music.
    """
    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a sentiment analysis expert. Extract the primary emotion from the text and respond with just one of the following emotion categories: 'happy', 'sad', 'energetic', 'relaxed', 'angry', 'romantic', 'focused', 'melancholic'. Only respond with the emotion word."},
                {"role": "user", "content": text}
            ],
            max_tokens=10,
            temperature=0.3
        )
        sentiment = response.choices[0].message.content.strip().lower()
        
        # Map to one of our predefined categories if not already
        valid_sentiments = ['happy', 'sad', 'energetic', 'relaxed', 'angry', 'romantic', 'focused', 'melancholic']
        
        if sentiment not in valid_sentiments:
            # Default fallback mapping based on valence
            # This is a simple mapping, could be improved
            sentiment_map = {
                'joyful': 'happy',
                'excited': 'energetic',
                'content': 'relaxed',
                'depressed': 'sad',
                'anxious': 'energetic',
                'calm': 'relaxed',
                'frustrated': 'angry',
                'loving': 'romantic',
                'concentrated': 'focused',
                'nostalgic': 'melancholic'
            }
            sentiment = sentiment_map.get(sentiment, 'happy')  # Default to happy if unmapped
        
        return sentiment
        
    except Exception as e:
        # Log the error
        print(f"Error analyzing sentiment: {str(e)}")
        # Return a default sentiment
        return "happy"