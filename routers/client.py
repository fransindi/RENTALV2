from fastapi import APIRouter, Depends
from db.database import get_db
from routers.schemas import ClientBase
from sqlalchemy.orm import Session
from db import db_client

router = APIRouter(prefix="/client", tags=["client"])


@router.post("/")
def create_client(request: ClientBase, db: Session = Depends(get_db)):
    return db_client.create_client(db, request)


@router.get("/all")
def get_all(db: Session = Depends(get_db)):
    return db_client.get_all(db)


@router.get("/{id}")
def get_client(id: int, db: Session = Depends(get_db)):
    return db_client.get_client(db, id)
