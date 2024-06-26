from sqlalchemy.orm import Session
from routers.schemas import EquipmentBase
from db.models import DbCategory, DbEquipment, DbTypo
from fastapi import HTTPException, status


def create_equipment(db: Session, request: EquipmentBase):
    category = db.query(DbCategory).filter(DbCategory.id == request.category_id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )

    typo = db.query(DbTypo).filter(DbTypo.id == request.typo_id).first()
    if not typo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Typo not found"
        )

    price = typo.base_price * category.rate

    equipment = DbEquipment(
        name=request.name,
        brand=request.brand,
        size=request.size,
        category_id=request.category_id,
        typo_id=request.typo_id,
        available=True,
        price=price,
    )
    db.add(equipment)
    db.commit()
    db.refresh(equipment)
    return equipment


def get_all(db: Session):
    return db.query(DbEquipment).all()


def get_equipment(db: Session, id: int):
    equipment = db.query(DbEquipment).filter(DbEquipment.id == id).first()
    if not equipment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Equipment id not found"
        )
    return equipment


def delete_equipment(db: Session, id: int):
    equipment = get_equipment(db, id)
    db.delete(equipment)
    db.commit()
    return "Equipment deleted"
