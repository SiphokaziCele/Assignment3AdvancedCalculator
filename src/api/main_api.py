from fastapi import FastAPI
from src.api.user_routes import router as user_router


app = FastAPI(title="Advanced Calculator API")

app.include_router(user_router)
