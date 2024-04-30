from db.database import Base
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Date,
    Float,
    Boolean,
    Table,
)
from sqlalchemy.orm import relationship


# TABLE USER
class DbUser(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    franchise_id = Column(Integer, ForeignKey("franchise.id"))

    franchise = relationship("DbFranchise", back_populates="user")


# TABLE FRANCHISE
class DbFranchise(Base):
    __tablename__ = "franchise"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)

    user = relationship("DbUser", back_populates="franchise")


# TABLE MANY TO MANY MEMBER-EQUIPMENT
member_equipment = Table(
    "member_equipment",
    Base.metadata,
    Column("member_id", Integer, ForeignKey("member.id")),
    Column("equipment_id", Integer, ForeignKey("equipment.id")),
)


# TABLE EQUIPMENT
class DbEquipment(Base):
    __tablename__ = "equipment"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    brand = Column(String)
    size = Column(Float)
    category_id = Column(Integer, ForeignKey("category.id"))
    typo_id = Column(Integer, ForeignKey("typo.id"))
    available = Column(Boolean)
    price = Column(Float)

    category = relationship("DbCategory", back_populates="equipment")
    typo = relationship("DbTypo", back_populates="equipment")
    member = relationship(
        "DbMember", secondary=member_equipment, back_populates="equipment"
    )


# TABLE CATEGORY
class DbCategory(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    rate = Column(Float)

    equipment = relationship("DbEquipment", back_populates="category")


# TABLE TYPO
class DbTypo(Base):
    __tablename__ = "typo"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    base_price = Column(Integer)

    equipment = relationship("DbEquipment", back_populates="typo")


# TABLE RESERVATION
class DbReservation(Base):
    __tablename__ = "reservation"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("client.id"))
    rental_begins = Column(Date)
    days = Column(Integer)

    member = relationship("DbMember", back_populates="reservation")
    client = relationship("DbClient", back_populates="reservation")
    contract = relationship("DbContract", back_populates="reservation")


# TABLE CLIENT
class DbClient(Base):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact = Column(String)

    reservation = relationship("DbReservation", back_populates="client")


# TABLE MEMBER
class DbMember(Base):
    __tablename__ = "member"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    reservation_id = Column(Integer, ForeignKey("reservation.id"))

    equipment = relationship(
        "DbEquipment", secondary=member_equipment, back_populates="member"
    )
    reservation = relationship("DbReservation", back_populates="member")


# TABLE CONTRACT
class DbContract(Base):
    __tablename__ = "contract"
    id = Column(Integer, primary_key=True, index=True)
    rental_begins = Column(Date)
    rental_ends = Column(Date)
    reservation_id = Column(Integer, ForeignKey("reservation.id"))
    price = Column(Float)

    reservation = relationship("DbReservation", back_populates="contract")
