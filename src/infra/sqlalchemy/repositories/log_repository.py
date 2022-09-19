from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import now
from src.infra.sqlalchemy.models import models


class LogRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, user_id: int, travel_id: int, action: str, value: float):
        log_bd = models.Log(
            user_id=user_id,
            travel_id=travel_id,
            action=action,
            value=value,
            created_at=now(),
        )

        self.session.add(log_bd)
        self.session.commit()
        self.session.refresh(log_bd)
        return log_bd

    def list_travel_logs(self, travel_id: int):
        statement = select(models.Log).where(models.Log.travel_id == travel_id)
        logs = self.session.execute(statement).scalars().all()
        print(logs[0].created_at, logs[0].user_id, logs[0].travel_id, logs[0].action, logs[0].value, logs[0].log_id)
        return logs

    def list_user_logs(self, user_id: int):
        statement = select(models.Log).where(models.Log.user_id == user_id)
        logs = self.session.execute(statement).scalars().all()
        return logs
