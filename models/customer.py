#!/usr/bin/python
"""
The customers table
A customer is a user that can posts items and cargos that needed to be
transport from city to other
"""
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Customer(BaseModel, Base):
    """Customers table"""
    __tablename__ = 'customers'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    company = Column(String(128), nullable=True)
    user = relationship("User")
