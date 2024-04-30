from sqlalchemy.orm import Session

from db.models import DbReservation, DbMember, DbContract
from fastapi import HTTPException, status
from datetime import timedelta


def create_contract(db: Session, reservation_id: int):
    reservation = (
        db.query(DbReservation).filter(DbReservation.id == reservation_id).first()
    )
    if not reservation:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Reservation_id Dont found"
        )
    rental_ends = reservation.rental_begins + timedelta(days=reservation.days)
    members = db.query(DbMember).filter(DbMember.reservation_id == reservation.id).all()
    if not members:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No members in this reservation.",
        )

    prices = []
    for i in members:
        miembro = db.query(DbMember).get(i.id)
        for j in miembro.equipment:
            prices.append(round(j.price, 2))

    price = sum(prices) * reservation.days

    new_contract = DbContract(
        rental_begins=reservation.rental_begins,
        rental_ends=rental_ends,
        reservation_id=reservation.id,
        price=price,
    )
    db.add(new_contract)
    db.commit()
    db.refresh(new_contract)
    return new_contract


def get_contract(db: Session, id: int):
    return db.query(DbContract).filter(DbContract.id == id).first()
