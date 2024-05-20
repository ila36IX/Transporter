#!/usr/bin/python3
"""Represets drivers table
Driver is a 'user' that drives a vehicle
"""
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from hashlib import md5
from sqlalchemy import Column, String, Date, Integer, ForeignKey
import enum
from sqlalchemy import Enum
from sqlalchemy import event

class MyEnum(enum.Enum):
    one = 1
    two = 2
    three = 3

class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'users'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    current_location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    license_num = Column(String(128), nullable=True)
    status = Column(ENUM(states)
