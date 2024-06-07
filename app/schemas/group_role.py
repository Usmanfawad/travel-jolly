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
        populate_by_name = True
        from_attributes = True
