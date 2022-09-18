from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.schemas import Travel, SimpleTravel, ActionModel
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.travel_repository import TravelRepository

router = APIRouter()


@router.post("/travel", status_code=status.HTTP_201_CREATED, response_model=Travel)
def create_travel(travel: SimpleTravel, session: Session = Depends(get_db)):
    new_travel = TravelRepository(session).create(travel)
    return new_travel


@router.get("/travel/{travel_id}", response_model=Travel)
def get_travel_by_id(travel_id: int, session: Session = Depends(get_db)):
    find_travel = TravelRepository(session).get_travel_by_id(travel_id)

    if not find_travel:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"There is no travel with id = {travel_id}",
        )

    return find_travel


@router.put("/travel/{travel_id}", response_model=Travel)
def atualizar_produto(
    travel_id: int,
    action_params: ActionModel,
    session: Session = Depends(get_db),
):

    find_travel = TravelRepository(session).get_travel_by_id(travel_id)

    if not find_travel:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"There is no travel with id = {travel_id}",
        )

    new_price = get_new_price(
        action_params.number, find_travel.price, action_params.action
    )

    if new_price is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Action not found"
        )

    TravelRepository(session).update(travel_id, new_price)
    return TravelRepository(session).get_travel_by_id(travel_id)


def get_new_price(number: float, price: float, action: str):
    try:
        if action == "sum":
            return price + number
        elif action == "sub":
            return price - number
        elif action == "mult":
            return price * number
        elif action == "div":
            return price / number
        else:
            return None
    except Exception:
        return None


@router.delete("/travel/{travel_id}")
def remover_produto(travel_id: int, session: Session = Depends(get_db)):
    is_deleted = TravelRepository(session).delete_by_id(travel_id)

    if not is_deleted:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"travel not found"
        )

    return {"message": "Produto removido com sucesso"}
