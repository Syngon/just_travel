import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from src.infra.sqlalchemy.config.database import Base


class Travel(Base):
    __tablename__ = 'travel'

    id: Column(Integer, primary_key=True, index=True)
    user_id: Column(Integer, ForeignKey('user.id'))
    name: Column(String)
    place: Column(String)
    price: Column(Float)
    created_at: Column(DateTime)

class User(Base):
    __tablename__ = 'user'

    id: Column(Integer, primary_key=True, index=True)
    username: Column(String)
    password: Column(String)
    is_active: Column(Boolean)
    created_at: Column(DateTime, default=datetime.datetime.utcnow)


class Log(Base):
    __tablename__ = 'log'

    user_id: Column(String)
    travel_id: Column(String)
    action: Column(String)
    value: Column(float)
    created_at: Column(DateTime)