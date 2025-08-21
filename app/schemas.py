import numpy as np
from pydantic import BaseModel

class InputData(BaseModel):
    array: list[float]

class OutputData(BaseModel):
    status: bool
    data: int | None = None
    message: str | None = None