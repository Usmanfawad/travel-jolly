from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict   

class UserBase(BaseModel):
    password: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    id: str = Field(..., alias="_id")


class User(UserBase):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True
        orm_mode: True
