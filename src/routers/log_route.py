from fastapi import APIRouter, status, Depends, HTTPException, BackgroundTasks
from src.schemas.schemas import Log, LogData
from src.infra.sqlalchemy.config.database import get_db
from src.services.write_notification import write_notification
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositories.log_repository import LogRepository
from typing import List


router = APIRouter()


@router.post("/log/")
def log(json_log: LogData, background: BackgroundTasks):

    data_is_correct = check_data_types(json_log)

    if not data_is_correct:
        return {"Error": "Data is incorrect"}

    background.add_task(
        write_notification,
        user_id=json_log.user_id,
        travel_id=json_log.travel_id,
        action=json_log.action,
        value=json_log.value,
    )
    return {"OK": "Mensagem enviada"}


def check_data_types(json_log: LogData):
    if not isinstance(json_log.user_id, int):
        return False
    if not isinstance(json_log.travel_id, int):
        return False
    if not isinstance(json_log.action, str):
        return False
    if not isinstance(json_log.value, float):
        return False
    return True
