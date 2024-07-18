from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr


class User(UserBase):
    id: str = Field(default_factory=str, alias="_id")

    