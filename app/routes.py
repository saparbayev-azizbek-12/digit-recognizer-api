import numpy as np
from fastapi import APIRouter
from services import predict
from schemas import InputData, OutputData

router = APIRouter()

@router.post("/", response_model=OutputData)
def index(data: InputData):
    arr = np.array(data.array, dtype=float)
    arr = arr.reshape(1,784)
    pred = predict(arr)
    try:
        if pred:
            res = {
                "status": True,
                "data": pred
            }
            return res
        else:
            return {"status": False}
    except Exception as e:
        res = {
            "status": False,
            "message": e 
        }