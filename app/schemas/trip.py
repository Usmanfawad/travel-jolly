from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional

class TripBase(BaseModel):
    name: str
    location: str
    description: str
    start_date: date
    end_date: date
    budget: Optional[float] = None

class TripCreate(TripBase):
    pass

class TripUpdate(TripBase):
    pass

class Trip(TripBase):
    id: str = Field(..., alias="_id")
    user_id: str
    created_date: datetime

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
