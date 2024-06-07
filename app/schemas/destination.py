from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional, Dict


class Suggestion(BaseModel):
    name: str
    description: Optional[str]


class DestinationBase(BaseModel):
    trip_id: str
    name: str
    description: Optional[str]
    start_date: date
    end_date: date
    destination_type: str
    suggestions: Optional[List[Suggestion]] = []


class DestinationCreate(DestinationBase):
    pass


class Destination(DestinationBase):
    id: str = Field(..., alias="_id")

    class Config:
        populate_by_name = True
        from_attributes = True
