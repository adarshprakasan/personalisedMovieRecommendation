import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("API_KEY")
if not openai.api_key:
    raise ValueError("API_KEY not found. Please set it in the .env file.")

def get_recommendations(user_movies):
    """
    Generate movie recommendations using traditional filtering and LLM.
    """
    # Placeholder for traditional recommendation logic
    traditional_recommendations = ["Interstellar", "Frozen II", "Shutter Island"]

    # Generate LLM-based recommendations
    prompt = f"""
    User's favorite movies: {user_movies}.
    Recommend 5 additional movies from this list: {traditional_recommendations}.
    Explain each recommendation in detail.
    """
    try:
        response = openai.ChatCompletion.create(
             model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        raise RuntimeError(f"Failed to fetch recommendations from OpenAI API: {str(e)}")
