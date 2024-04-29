from fastapi import APIRouter, HTTPException, status, Depends
from db.database import get_db
from routers.schemas import ClientBase
from sqlalchemy.orm import Session
from db import db_client
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/client',
    tags=['client']
)

@router.post('/')
def create_client(request: ClientBase, db: Session = Depends(get_db)):
    return db_client.create_client(db, request)