from sqlalchemy.orm import Session
from routers.schemas import ReservationBase
from db.models import DbReservation, DbClient
from fastapi import HTTPException, status


def create_reservation(db: Session, request: ReservationBase):
    client = db.query(DbClient).filter(DbClient.id == request.client_id).first()
    if not client:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Client ID"
        )

    client_reservation = db.query(DbReservation).filter(
        DbReservation.client_id == client.id
    )
    if client_reservation:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Client have a reservation pending.",
        )

    if request.days <= 0:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Days cant be less than 0"
        )

    reservation = DbReservation(
        client_id=request.client_id,
        rental_begins=request.rental_begin,
        days=request.days,
    )
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation
