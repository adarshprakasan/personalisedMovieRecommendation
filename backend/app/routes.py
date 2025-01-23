from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services import get_recommendations

router = APIRouter()

class UserMovies(BaseModel):
    movies: list[str] 

@router.post("/recommend")
async def recommend_movies(user_movies: UserMovies):
    """
    Recommend movies based on user inputs.
    """
    try:
        recommendations = get_recommendations(user_movies.movies)
        return {"recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
