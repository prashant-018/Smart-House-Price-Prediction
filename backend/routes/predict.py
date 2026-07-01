from fastapi import APIRouter
from schemas.house_schema import HouseData
import joblib
import numpy as np
import os

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

model = joblib.load(os.path.join(BASE_DIR, "ml", "model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "ml", "scaler.pkl"))


@router.post("/predict")
def predict(data: HouseData):

    values = np.array([[
        data.OverallQual,
        data.GrLivArea,
        data.GarageCars,
        data.GarageArea,
        data.TotalBsmtSF,
        data.FullBath,
        data.YearBuilt,
        data.YearRemodAdd,
        data.LotArea,
        data.BedroomAbvGr
    ]])

    values = scaler.transform(values)

    prediction = model.predict(values)[0]

    return {
        "PredictedPrice": round(float(prediction), 2)
    }