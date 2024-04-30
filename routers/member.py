from fastapi import APIRouter, Depends
from db.database import get_db
from routers.schemas import MemberBase
from sqlalchemy.orm import Session
from db import db_member


router = APIRouter(prefix="/member", tags=["member"])


@router.post("/")
def create_member(request: MemberBase, db: Session = Depends(get_db)):
    return db_member.create_member(db, request)


@router.get("/by_reservation/{id}")
def get_members_by_reservation(reservation_id: int, db: Session = Depends(get_db)):
    return db_member.get_members_by_reservation(db, reservation_id)
