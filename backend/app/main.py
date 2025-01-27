from fastapi import FastAPI
from app.routers import recommend
from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI(
#     title="Personalized Movie Recommendation System",
#     version="1.0.0",
#     description="A system that recommends movies based on user preferences."
# )

app = FastAPI()

origins = [
    "http://localhost:5173", 
    "http://127.0.0.1:5173", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_credentials=True,        
    allow_methods=["*"],           
    allow_headers=["*"],            
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Movie Recommendation API!"}

# Include the recommendation router
app.include_router(recommend.router)
