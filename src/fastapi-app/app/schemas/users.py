from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    fullname: str | None = None


class UserResponce(BaseModel):
    id: int
    email: str
    username: str
    fullname: str | None

    is_active: bool
    is_verified: bool

    created_at: datetime
    updated_at: datetime | None
    last_login: datetime | None

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    username: str | None = None
    fullname: str | None = None


class UserLogin(BaseModel):
    email: str
    password: str
