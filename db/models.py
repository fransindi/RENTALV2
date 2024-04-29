from db.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Enum, Float, Boolean, Table
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    franchise_id = Column(Integer, ForeignKey('franchise.id'))

    franchise = relationship('DbFranchise', back_populates='user')

class DbFranchise(Base):
    __tablename__ = 'franchise'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)

    user = relationship('DbUser', back_populates='franchise')


member_equipment = Table('member_equipment', Base.metadata,
    Column('member_id', Integer, ForeignKey('member.id')),
    Column('equipment_id', Integer, ForeignKey('equipment.id'))
    )



class DbEquipment(Base):
    __tablename__ = 'equipment'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    brand = Column(String)
    size = Column(Float)
    category_id = Column(Integer, ForeignKey('category.id'))
    typo_id = Column(Integer, ForeignKey('typo.id'))
    available = Column(Boolean)
    price = Column(Float)

    category = relationship('DbCategory', back_populates='equipment')
    typo = relationship('DbTypo', back_populates='equipment')
    member = relationship('DbMember', secondary=member_equipment, back_populates='equipment')

class DbCategory(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    rate = Column(Float)

    equipment = relationship('DbEquipment', back_populates='category')

class DbTypo(Base):
    __tablename__ = 'typo'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    base_price = Column(Integer)

    equipment = relationship('DbEquipment', back_populates='typo')



class DbReservation(Base):
    __tablename__ = 'reservation'
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    rental_begins = Column(Date)
    days = Column(Integer)

    client = relationship('DbClient', back_populates='reservation')

class DbClient(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact = Column(String)

    reservation = relationship('DbReservation', back_populates='client')



class DbMember(Base):
    __tablename__ = 'member'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    equipment = relationship("DbEquipment", secondary=member_equipment, back_populates="member")


