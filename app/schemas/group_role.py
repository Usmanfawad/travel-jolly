from pydantic import BaseModel, Field
from typing import List, Literal

class RoleBase(BaseModel):
    role_name: str
    permissions: List[Literal["create","read","update","delete"]] = None

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass
class Role(RoleBase):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
