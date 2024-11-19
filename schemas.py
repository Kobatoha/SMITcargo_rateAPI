from pydantic import BaseModel
from datetime import date


class InsuranceRateCreate(BaseModel):
    date: date
    cargo_type: str
    rate: float


class InsuranceRateResponse(BaseModel):
    insurance_cost: float
