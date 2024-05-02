from fastapi import APIRouter, Depends
from db.database import get_db
from routers.schemas import MemberBase
from sqlalchemy.orm import Session
from db import db_member


router = APIRouter(prefix="/member", tags=["member"])


@router.post("/",
            response_description='The new member created with a list of equipments_ids.',
            summary='Creates a new member and link this with the list of equipments ids. ')
def create_member(request: MemberBase, db: Session = Depends(get_db)):
    return db_member.create_member(db, request)


@router.get("/by_reservation/{id}",
            response_description='List of members in a reservation',
            summary='Retrieve all the members in a specific reservation.')
def get_members_by_reservation(reservation_id: int, db: Session = Depends(get_db)):
    return db_member.get_members_by_reservation(db, reservation_id)
