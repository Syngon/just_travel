from datetime import datetime
from pydantic import BaseModel
from typing import List

class Travel(BaseModel):
    id: int
    user_id: int
    name: str
    place: str
    price: float
    created_at: datetime

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    username: str
    password: str
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class Log(BaseModel):
    user_id: str
    travel_id: str
    action: str
    value: float
    created_at: datetime


class LoginData(BaseModel):
    password: str
    username: str


class LoginSuccess(BaseModel):
    user: User
    access_token: str