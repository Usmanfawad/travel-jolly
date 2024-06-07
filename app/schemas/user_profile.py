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
        populate_by_name = True
        from_attributes: True
