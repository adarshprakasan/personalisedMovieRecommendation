from fastapi import APIRouter, HTTPException
from app.models.movie import MovieRequest, RecommendationResponse
from app.utils.recommendation_engine import get_recommendations

router = APIRouter()

@router.post("/recommend", response_model=RecommendationResponse)
def recommend_movies(request: MovieRequest):
    try:
        recommendations = get_recommendations(request.movie)
        return {"recommended_movies": recommendations}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
