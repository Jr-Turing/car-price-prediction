from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .model import load_artifacts, predict_price
from .schema import CarFeatures, PredictionResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_artifacts()
    yield


app = FastAPI(title="Car Price Prediction API", version="1.0", lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later you can restrict to your streamlit domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def test():
    return JSONResponse(
        status_code=200, content={"success": True, "message": "this is test route"}
    )


@app.post("/predict", response_model=PredictionResponse)
def predict(features: CarFeatures):
    price = predict_price(features.model_dump())
    return PredictionResponse(prediction_price=price)
