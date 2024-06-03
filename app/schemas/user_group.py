from pydantic import BaseModel, Field
from typing import List, Dict

class GroupMember(BaseModel):
    user_id: str
    role_id: str  # Changed to reference role_id

class GroupBase(BaseModel):
    group_name: str
    members: List[GroupMember] = []
    trip_ids: List[str] = []

class GroupCreate(GroupBase):
    pass

class GroupUpdate(BaseModel):
    group_name: str = None
    members: List[GroupMember] = None
    trip_ids: List[str] = None

class Group(GroupBase):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
