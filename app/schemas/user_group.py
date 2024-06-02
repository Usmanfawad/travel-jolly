from pydantic import BaseModel, Field
from typing import List, Dict, Literal

class GroupMember(BaseModel):
    user_id: str
    role: Literal["admin", "member"]

class UserGroupBase(BaseModel):
    group_id: str
    group_name: str
    members: List[GroupMember]
    trip_ids: List[str]

class UserGroupCreate(UserGroupBase):
    pass

class UserGroupUpdate(BaseModel):
    group_name: str
    members: List[GroupMember]
    trip_ids: List[str]

class UserGroup(UserGroupBase):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True
        orm_mode: True
