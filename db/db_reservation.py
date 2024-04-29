from sqlalchemy.orm import Session
from routers.schemas import ReservationBase
from db.models import DbReservation, DbClient
from fastapi import HTTPException, status
from datetime import date

def create_reservation(db: Session, request: ReservationBase):
    client = db.query(DbClient).filter(DbClient.id == request.client_id).first()
    if not client:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Client ID')
    reservation = DbReservation(
        client_id = request.client_id,
        rental_begins = request.rental_begin,
        days = request.days
    )
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation
