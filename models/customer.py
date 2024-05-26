#!/usr/bin/python
"""
The customers table
A customer is a user that can posts items and cargos that needed to be
transport from city to other
"""
import sqlalchemy
from models import *
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Customer(BaseModel, Base):
    """Customers table"""
    __tablename__ = 'customers'
    user_id = Column(
        Integer,
        ForeignKey('users.id', name="fk_user0customer"),
        nullable=False
    )
    company = Column(String(128), nullable=True)
    user = relationship(
        "User",
        cascade="all, delete-orphan",
        single_parent=True
    )
    ratings = relationship(
        "Rating",
        backref="customer",
        cascade="all, delete-orphan",
    )
