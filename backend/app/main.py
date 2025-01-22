from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Personalized Movie Recommendation System",
    version="1.0.0",
    description="A system that recommends movies based on user preferences."
)

# Include API routes
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Movie Recommendation API!"}
