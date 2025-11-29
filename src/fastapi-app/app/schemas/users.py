from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    fullname: Optional[str] = None


class UserResponce(BaseModel):
    id: int
    email: str
    username: str
    fullname: Optional[str]

    is_active: bool
    is_verified: bool

    created_at: datetime
    updated_at: Optional[datetime]
    last_login: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    fullname: Optional[str] = None


class UserLogin(BaseModel):
    email: str
    password: str
