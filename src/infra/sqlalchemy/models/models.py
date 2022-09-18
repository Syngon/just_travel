from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.sql.functions import now
from src.infra.sqlalchemy.config.database import Base


class Travel(Base):
    __tablename__ = "travel"

    travel_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    name = Column(String)
    place = Column(String)
    price = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=now())

    # TODO CREATE VALIDATOR


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    is_active = Column(Boolean)
    created_at = Column(DateTime(timezone=True), server_default=now())

    # TODO CREATE VALIDATOR


class Log(Base):
    __tablename__ = "log"

    log_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    travel_id = Column(Integer)
    action = Column(String)
    value = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=now())
