from pydantic import BaseModel
import datetime

class Weight(BaseModel):
    id: int
    date: datetime.date
    weight: float

class WeightCreate(BaseModel):
    date: datetime.date
    weight: float