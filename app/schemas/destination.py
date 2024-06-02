from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, List, Dict

class DestinationBase(BaseModel):
    destination_id: str
    trip_id: str
    name: str
    description: str
    start_date: date
    end_date: date
    destination_type: str
    suggestions: Optional[List[Dict]] = None

class DestinationCreate(DestinationBase):
    pass

class DestinationUpdate(BaseModel):
    name: str
    description: str
    start_date: date
    end_date: date
    destination_type: str
    suggestions: Optional[List[Dict]] = None

class Destination(DestinationBase):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True
        orm_mode: True
