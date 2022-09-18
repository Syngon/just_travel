from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# from src.infra.sqlalchemy.models.models import Travel
from src.schemas.schemas import Travel
from src.schemas.schemas import UserWithIdAndUsername
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.user_repository import UserRepository

router = APIRouter()


@router.get("/user/travels", response_model=List[Travel])
def list_user_travels(user_id: int, session: Session = Depends(get_db)):
    find_travels = UserRepository(session).list_user_travels(user_id)

    if not find_travels:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"There is no travels for this user",
        )

    return find_travels


@router.get("/user/{user_id}", response_model=UserWithIdAndUsername)
def get_user_by_id(user_id: int, session: Session = Depends(get_db)):
    find_user = UserRepository(session).get_user_by_id(user_id)
    if not find_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There is no user with id = {user_id}",
        )

    return find_user
