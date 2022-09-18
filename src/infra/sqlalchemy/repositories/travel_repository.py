from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import now
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class TravelRepository():

    def __init__(self, session: Session):
        self.session = session

    def create(self, travel: schemas.Travel):
        travel_bd = models.Travel(name=travel.username,
                                    place=travel.place,
                                    price=travel.price,
                                    created_at= now())

        self.session.add(travel_bd)
        self.session.commit()
        self.session.refresh(travel_bd)
        return travel_bd

    def get_travel_by_id(self, travel_id: int):
        statement = select(models.Travel).where(models.Travel.travel_id == travel_id)
        travel = self.session.execute(statement).scalars().first()
        return travel

    def update(self, travel_id: int, new_price: float):
        find_travel = self.get_travel_by_id(travel_id)
        if not find_travel:
            return False

        statement = update(models.Travel).where(models.Travel.travel_id == travel_id).values(price=new_price)
        self.session.execute(statement)
        self.session.commit()
        return self.get_travel_by_id(travel_id)

    def delete_by_id(self, travel_id: int):

        find_travel = self.get_travel_by_id(travel_id)
        if not find_travel:
            return False

        statement = delete(models.Travel).where(models.Travel.travel_id == travel_id)
        self.session.execute(statement)
        self.session.commit()

        return True