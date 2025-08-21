from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="ML Model Prediction")
app.include_router(router, tags=["Prediction"])