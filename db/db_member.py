from sqlalchemy.orm import Session

from db.models import DbMember, DbEquipment
from fastapi import HTTPException, status


def create_member(db: Session, request: DbMember):
    if request.equipent_ids == []:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Your list is empty"
        )

    nuevo_miembro = DbMember()
    for id_equipment in request.equipment_ids:
        item = db.query(DbEquipment).filter(DbEquipment.id == id_equipment).first()
        if item:
            nuevo_miembro.name = request.name
            nuevo_miembro.equipment.append(item)
            nuevo_miembro.reservation_id = request.reservation_id
            item.available = False

    db.add(nuevo_miembro)
    db.commit()
    db.refresh(nuevo_miembro)
    return nuevo_miembro


def get_members_by_reservation(db: Session, reservation_id: int):
    members = db.query(DbMember).filter(DbMember.reservation_id == reservation_id).all()
    if not members:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No members in this reservation.",
        )
    return members
