from fastapi import APIRouter, status, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from src.schemas.schemas import LogData
from src.services.write_notification import write_notification
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


async def verify_and_log(
    action_params: ActionModel,
    travel_id: int,
    background: BackgroundTasks,
    session: Session = Depends(get_db),
):

    find_travel = TravelRepository(session).get_travel_by_id(travel_id)
    if not find_travel:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"There is no travel with id = {travel_id}",
        )

    data_is_correct = check_data_types(action_params, find_travel)
    if not data_is_correct:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Data is incorrect"
        )

    background.add_task(
        write_notification,
        user_id=find_travel.user_id,
        travel_id=find_travel.travel_id,
        action=action_params.action,
        value=action_params.value,
    )
    return action_params


def check_data_types(action_params: ActionModel, find_travel: Travel):
    if not isinstance(find_travel.user_id, int):
        return False
    if not isinstance(find_travel.travel_id, int):
        return False
    if not isinstance(action_params.action, str):
        return False
    if not isinstance(action_params.value, float):
        return False
    return True


@router.put(
    "/travel/{travel_id}", response_model=Travel, dependencies=[Depends(verify_and_log)]
)
def atualizar_produto(
    travel_id: int,
    action_params: ActionModel,
    background: BackgroundTasks,
    session: Session = Depends(get_db),
):

    find_travel = TravelRepository(session).get_travel_by_id(travel_id)
    new_price = get_new_price(
        action_params.value, find_travel.price, action_params.action
    )

    if new_price is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Action not found"
        )

    TravelRepository(session).update(travel_id, new_price)
    return TravelRepository(session).get_travel_by_id(travel_id)


def get_new_price(value: float, price: float, action: str):
    try:
        if action == "sum":
            return price + value
        elif action == "sub":
            return price - value
        elif action == "mult":
            return price * value
        elif action == "div":
            return price / value
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
