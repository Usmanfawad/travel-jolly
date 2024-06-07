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
        populate_by_name = True
        from_attributes = True
