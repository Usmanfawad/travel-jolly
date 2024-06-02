from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class ActivityBase(BaseModel):
    activity_id: str
    destination_id: str
    name: str
    description: str
    suggestions: Optional[List[Dict]] = None

class ActivityCreate(ActivityBase):
    pass

class ActivityUpdate(BaseModel):
    name: str
    description: str
    suggestions: Optional[List[Dict]] = None

class Activity(ActivityBase):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True
        orm_mode: True
