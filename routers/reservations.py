from fastapi import APIRouter, Depends
from db.database import get_db
from routers.schemas import ReservationBase
from sqlalchemy.orm import Session
from db import db_reservation


router = APIRouter(prefix="/reservation", tags=["reservation"])


@router.post("/")
def create_reservation(request: ReservationBase, db: Session = Depends(get_db)):
    return db_reservation.create_reservation(db, request)
