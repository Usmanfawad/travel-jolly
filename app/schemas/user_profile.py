from pydantic import BaseModel, Field
from typing import Dict, List

class UserProfileBase(BaseModel):
    user_id: str
    travel_preferences: Dict[str, List[str]]

class UserProfileCreate(UserProfileBase):
    pass

class UserProfileUpdate(BaseModel):
    travel_preferences: Dict[str, List[str]]

class UserProfile(UserProfileBase):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True
        orm_mode: True
