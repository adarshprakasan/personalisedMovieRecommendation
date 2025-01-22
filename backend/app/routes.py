from fastapi import APIRouter
from app.services import get_recommendations

router = APIRouter()

@router.post("/recommend")
async def recommend_movies(user_movies: list):
    """
    Recommend movies based on user inputs.
    """
    recommendations = get_recommendations(user_movies)
    return {"recommendations": recommendations}
