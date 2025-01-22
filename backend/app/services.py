import openai

# Your OpenAI API key
openai.api_key = "your_openai_api_key"

def get_recommendations(user_movies):
    """
    Generate movie recommendations using traditional filtering and LLM.
    """
    # Placeholder for traditional recommendation logic
    # Replace with actual collaborative/content-based filtering
    traditional_recommendations = ["Interstellar", "Frozen II", "Shutter Island"]

    # Generate LLM-based recommendations
    prompt = f"""
    User's favorite movies: {user_movies}.
    Recommend 5 additional movies from this list: {traditional_recommendations}.
    Explain each recommendation in detail.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']
