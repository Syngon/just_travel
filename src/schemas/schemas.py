from datetime import datetime
import string
from typing import List
from pydantic import BaseModel


class Travel(BaseModel):
    travel_id: int
    user_id: int
    name: str
    place: str
    price: float
    created_at: datetime

    class Config:
        orm_mode = True


class SimpleTravel(BaseModel):
    user_id: int
    name: str
    place: str
    price: float

    class Config:
        orm_mode = True


class TravelList(BaseModel):
    travels: List[Travel]


class UserWithIdAndUsername(BaseModel):
    user_id: int
    username: str

    class Config:
        orm_mode = True


class User(BaseModel):
    user_id: int
    username: str
    password: str
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True


class SimpleUser(BaseModel):
    username: str
    password: str


class ActionModel(BaseModel):
    value: float
    action: str


class Log(BaseModel):
    user_id: str
    travel_id: str
    action: str
    value: float
    created_at: datetime


class LogData(BaseModel):
    user_id: int
    travel_id: int
    action: str
    value: int


class LoginData(BaseModel):
    password: str
    username: str


class LoginSuccess(BaseModel):
    user: UserWithIdAndUsername
    access_token: str
