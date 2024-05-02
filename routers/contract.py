from fastapi import APIRouter, Depends
from db.database import get_db
from sqlalchemy.orm import Session
from db import db_contract


router = APIRouter(prefix="/contract", tags=["contract"])


@router.post(
    "/{id}",
    response_description="The info of the new contract in a json format.",
    summary="Given an reservation_id it creates a new contract.",
)
def create_contract(reservation_id: int, db: Session = Depends(get_db)):
    return db_contract.create_contract(db, reservation_id)


@router.get(
    "/{id}",
    response_description="Info of the contract in json format",
    summary="Retrieve a single contract with the id.",
)
def get_contract(id: int, db: Session = Depends(get_db)):
    return db_contract.get_contract(db, id)
