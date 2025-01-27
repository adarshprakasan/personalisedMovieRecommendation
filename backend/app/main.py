from fastapi import FastAPI
from app.routers import recommend

app = FastAPI()

origins = [
    "http://localhost:5173", 
    "http://127.0.0.1:5173", 
]

# Include the recommendation router
app.include_router(recommend.router)
