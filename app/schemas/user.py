from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict   

class UserBase(BaseModel):
    password: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    id: str = Field(..., alias="_id")


class User(UserBase):
    id: str = Field(..., alias="_id")

    class Config:
        populate_by_name = True
        from_attributes: True
