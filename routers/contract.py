from fastapi import APIRouter, Depends
from db.database import get_db
from sqlalchemy.orm import Session
from db import db_contract


router = APIRouter(prefix="/contract", tags=["contract"])


@router.post("/{id}")
def create_contract(reservation_id: int, db: Session = Depends(get_db)):
    return db_contract.create_contract(db, reservation_id)


@router.get("/{id}")
def get_contract(id: int, db: Session = Depends(get_db)):
    return db_contract.get_contract(db, id)
