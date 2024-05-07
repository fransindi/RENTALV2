from fastapi import APIRouter, Depends
from db.database import get_db
from routers.schemas import ReservationBase
from sqlalchemy.orm import Session
from db import db_reservation


router = APIRouter(prefix="/reservation", tags=["reservation"])


@router.post(
    "/",
    response_description="the reservation info in json format.",
    summary="Creates a new reservation.",
)
def create_reservation(request: ReservationBase, db: Session = Depends(get_db)):
    return db_reservation.create_reservation(db, request)


@router.get(
    "/all",
    response_description="List of all the reservations",
    summary="Retrieves all the information in the Reservation Table.",
)
def get_all_reservation(db: Session = Depends(get_db)):
    return db_reservation.get_all(db)

@router.get(
    "/{id}",
    response_description="Information about an specific reservation",
    summary="Retrieve the information of a reservation.",
)
def get_reservation(id: int, db: Session = Depends(get_db)):
    return db_reservation.get_reservation(db, id)


@router.delete(
    "/{id}",
    response_description="An error or okey message.",
    summary="Delete an specific reservation.",
)
def delete_reservation(id: int, db: Session = Depends(get_db)):
    return db_reservation.delete_reservation(db, id)
