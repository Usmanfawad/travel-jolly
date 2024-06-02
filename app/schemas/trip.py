from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class TripBase(BaseModel):
    trip_id: str
    user_id: str
    name: str
    location: str
    description: str
    start_date: date
    end_date: date
    created_date: date
    budget: Optional[float] = None

class TripCreate(TripBase):
    pass

class TripUpdate(BaseModel):
    name: str
    location: str
    description: str
    start_date: date
    end_date: date
    budget: Optional[float] = None

class Trip(TripBase):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True
        orm_mode: True
