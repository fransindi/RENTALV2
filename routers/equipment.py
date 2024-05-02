from fastapi import APIRouter, Depends
from db.database import get_db
from routers.schemas import EquipmentBase, EquipmentDisplay, UserAuth
from sqlalchemy.orm import Session
from db import db_equipment
from auth.oauth2 import get_current_user
from typing import List

router = APIRouter(prefix="/equipment", tags=["equipment"])


@router.post(
    "/",
    response_model=EquipmentDisplay,
    response_description="the info of the new equipment with his typo and category data",
    summary="Creates a new equipment.",
)
def create_equipment(
    request: EquipmentBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    return db_equipment.create_equipment(db, request)


@router.get(
    "/all",
    response_model=List[EquipmentDisplay],
    response_description="List with all the equipments.",
    summary="Retrieve all the equipments in the database.",
)
def get_all(db: Session = Depends(get_db)):
    return db_equipment.get_all(db)


@router.get(
    "/{id}",
    response_model=EquipmentDisplay,
    response_description="All the data of a specific equipment.",
    summary="Given an id it retrieves the data of the equipment.",
)
def get_equipment(id: int, db: Session = Depends(get_db)):
    return db_equipment.get_equipment(db, id)
