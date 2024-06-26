#!/usr/bin/python
"""
The locations table
Location is an exact position in a city
"""
import sqlalchemy
from models import *
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Location(BaseModel, Base):
    """Location table"""
    __tablename__ = 'locations'
    name = Column(String(128), nullable=False)
    city_id = Column(
        Integer, 
        ForeignKey('cities.id', name="fk_city_loc"),
        nullable=False
    )
