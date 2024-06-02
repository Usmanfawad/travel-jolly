from pydantic import BaseModel, Field
from typing import List

class GroupRoleBase(BaseModel):
    role_id: str
    role_name: str
    permissions: List[str]

class GroupRoleCreate(GroupRoleBase):
    pass

class GroupRoleUpdate(BaseModel):
    role_name: str
    permissions: List[str]

class GroupRole(GroupRoleBase):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True
        orm_mode: True
