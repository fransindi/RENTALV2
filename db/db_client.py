from sqlalchemy.orm import Session
from routers.schemas import ClientBase
from db.models import DbClient
from fastapi import HTTPException, status
from datetime import date


def create_client(db: Session, request: ClientBase):
    client = db.query(DbClient).filter(DbClient.name == request.name).first()
    if not client:
        client = DbClient(
            name = request.name,
            contact = request.contact
        )
        db.add(client)
        db.commit()
        db.refresh(client)
        return client
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Client already exist')

