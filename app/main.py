from fastapi import FastAPI
from routes import router

app = FastAPI(title="ML Model Prediction")
app.include_router(router, tags=["Prediction"])