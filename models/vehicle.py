#!/usr/bin/python
"""
The vehicles table
Vehicle is the machine the used by the driver to transport the items
"""
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, CheckConstraint, ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship


class Vehicle(BaseModel, Base):
    """vehicles table"""
    __tablename__ = 'vehicles'
    model = Column(String(300))
    year = Column(Integer, CheckConstraint('year >= 1900 AND year <= 2100'))
    capacity = Column(Integer)
    images = relationship(
        'Image',
        cascade="all, delete-orphan",
        single_parent=True
    )
