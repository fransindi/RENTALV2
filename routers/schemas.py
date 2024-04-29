from pydantic import BaseModel
from typing import Annotated
from fastapi import Query
from datetime import date


class UserAuth(BaseModel):
    id: int
    username: str
    email: str

class UserBase(BaseModel):
    username: Annotated[str, Query(min_length='3', max_length='20')]
    password: Annotated[str, Query(min_length='8', max_length='20')]
    franchise_id: int

# For UserDisplay
class FranchiseDisplay(BaseModel):
    id: int
    name: str
    location: str

class UserDisplay(BaseModel):
    username: str
    franchise: FranchiseDisplay


class EquipmentBase(BaseModel):
    name: str
    brand: str
    size: int
    category_id: int
    typo_id: int

# For Equipment Display
class CategoryBase(BaseModel):
    id: int
    name: str
    rate: float

# For Equipment Display
class TypoBase(BaseModel):
    id: int
    name: str
    base_price: int


class EquipmentDisplay(BaseModel):
    id: int
    name: str
    brand: str
    size: int
    category: CategoryBase
    typo: TypoBase
    price: float


class ReservationBase(BaseModel):
    client_id: int
    rental_begin: date
    days: int

class ClientBase(BaseModel):
    name: str
    contact: str