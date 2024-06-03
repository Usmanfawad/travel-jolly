from pydantic import BaseModel, Field
from typing import List

class RoleBase(BaseModel):
    role_name: str
    permissions: List[str]

class RoleCreate(RoleBase):
    pass

class RoleUpdate(BaseModel):
    role_name: str = None
    permissions: List[str] = None

class Role(RoleBase):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
