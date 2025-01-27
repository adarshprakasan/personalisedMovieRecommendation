from pydantic import BaseModel
from typing import List

class MovieRequest(BaseModel):
    movie: str

class Recommendation(BaseModel):
    title: str
    explanation: str

class RecommendationResponse(BaseModel):
    recommended_movies: List[Recommendation]
