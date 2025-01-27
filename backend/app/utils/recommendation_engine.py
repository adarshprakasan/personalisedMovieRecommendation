from app.database.data import MOVIE_DATABASE
from app.models.movie import Recommendation

def get_recommendations(input_movie: str):
    for movie in MOVIE_DATABASE:
        if movie["title"].lower() == input_movie.lower():
            input_tags = set(movie["tags"])
            break
    else:
        raise ValueError("Movie not found in the database.")

    recommendations = []
    for movie in MOVIE_DATABASE:
        if movie["title"].lower() != input_movie.lower():
            common_tags = input_tags.intersection(set(movie["tags"]))
            if common_tags:
                recommendations.append(
                    Recommendation(
                        title=movie["title"],
                        explanation=f"Recommended because it shares themes: {', '.join(common_tags)}",
                    )
                )

    return recommendations
