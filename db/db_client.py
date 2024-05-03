from sqlalchemy.orm import Session
from routers.schemas import ClientBase
from db.models import DbClient
from fastapi import HTTPException, status


def create_client(db: Session, request: ClientBase):
    client = db.query(DbClient).filter(DbClient.name == request.name).first()
    if not client:
        client = DbClient(name=request.name, contact=request.contact)
        db.add(client)
        db.commit()
        db.refresh(client)
        return client
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Client already exist"
    )


def get_all(db: Session):
    return db.query(DbClient).all()


def get_client(db: Session, id: int):
    client = db.query(DbClient).filter(DbClient.id == id).first()
    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Client dont found"
        )
    return client


def delete_client(db: Session, id: int):
    client = get_client(db, id)
    db.delete(client)
    db.commit()
    return "client deleted"
