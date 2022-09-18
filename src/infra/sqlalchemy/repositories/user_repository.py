from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import now
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class UserRepository():

    def __init__(self, session: Session):
        self.session = session

    def create(self, user: schemas.User):
        user_bd = models.User(username=user.username,
                                    password=user.password,
                                    is_active=True,
                                    created_at= now())

        self.session.add(user_bd)
        self.session.commit()
        self.session.refresh(user_bd)
        return user_bd

    def list_user_travels(self, user_id: int):
        statement = select(models.Travel).where(models.Travel.user_id == user_id)
        travels = self.session.execute(statement).scalars().all()
        return travels

    def get_user_by_id(self, user_id: int):
        statement = select(models.User).filter_by(user_id=user_id)
        user = self.session.execute(statement).scalars().first()
        return user

    def get_user_by_name(self, username: int):
        statement = select(models.User).filter_by(username=username)
        user = self.session.execute(statement)

        if not user:
            return False
        return user.scalars().first()
