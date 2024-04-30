from fastapi import APIRouter, Depends
from db.database import get_db
from routers.schemas import EquipmentBase, EquipmentDisplay, UserAuth
from sqlalchemy.orm import Session
from db import db_equipment
from auth.oauth2 import get_current_user
from typing import List

router = APIRouter(prefix="/equipment", tags=["equipment"])


@router.post("/", response_model=EquipmentDisplay)
def create_equipment(
    request: EquipmentBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    return db_equipment.create_equipment(db, request)


@router.get("/all", response_model=List[EquipmentDisplay])
def get_all(db: Session = Depends(get_db)):
    return db_equipment.get_all(db)


@router.get("/{id}", response_model=EquipmentDisplay)
def get_equipment(id: int, db: Session = Depends(get_db)):
    return db_equipment.get_equipment(db, id)
