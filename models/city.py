#!/usr/bin/python
"""Representation of the cities table"""
import sqlalchemy
from models import *
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Cities table"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    locations = relationship(
		"Location",
		backref="city",
		cascade="all, delete-orphan",
	)
