#!/usr/bin/python3
"""Represets drivers table
Driver is a 'user' that drives a vehicle
"""
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from hashlib import md5
from sqlalchemy import Column, String, Date, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship, backref
from sqlalchemy import event


class Driver(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'drivers'
    user_id = Column(
        Integer,
        ForeignKey('users.id', name="fk_dr_user"),
        nullable=False
    )
    current_location_id = Column(
        Integer,
        ForeignKey('locations.id', name="fk_dr_loc"),
        nullable=False
    )
    vehicle_id = Column(
        Integer,
        ForeignKey('vehicles.id', name="fk_dr_truck"),
        nullable=False
    )
    license_num = Column(String(128), nullable=True)
    status = Column(
        Enum('enroute', 'inactive', 'available', name='status_enum'),
        default="inactive"
    )
    vehicle = relationship(
        "Vehicle",
        backref=backref('driver', uselist=False),
        cascade="all, delete-orphan",
        uselist=False,
        single_parent=True
    )
    location = relationship("Location")
    user = relationship("User")
    deliveries = relationship(
        "Delivery",
        backref="driver",
        cascade="all, delete-orphan",
        single_parent=True
    )
