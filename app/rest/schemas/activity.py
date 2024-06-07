from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class ActivityBase(BaseModel):
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
        populate_by_name = True
        from_attributes: True
