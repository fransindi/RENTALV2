from sqlalchemy.orm import Session
from routers.schemas import UserBase
from db.models import DbUser, DbFranchise
from db.hash import Hash
from fastapi import HTTPException, status


def create_user(db: Session, request: UserBase):
    user = db.query(DbUser).filter(DbUser.username == request.username).first()
    if not user:
        franchise = db.query(DbFranchise).filter(DbFranchise.id == request.franchise_id).first()
        if not franchise:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Franchise not found')
        user = DbUser(
            username = request.username,
            password = Hash.bcrypt(request.password),
            franchise_id = request.franchise_id
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user