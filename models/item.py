#!/usr/bin/python
"""
Will be added soon!
"""
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship


class Item(BaseModel, Base):
    """items table"""
    __tablename__ = 'items'
    customer_id = Column(
        Integer, ForeignKey('customers.id', name="fk_item_customer"),
        nullable=False
    )
    pickup_location_id = Column(
        Integer,
        ForeignKey('locations.id', name="fk_plocitem"),
        nullable=False
    )
    dropoff_location_id = Column(
        Integer,
        ForeignKey('locations.id', name="fk_dloc_item"),
        nullable=False
    )
    description = Column(Text, nullable=True)
    weight = Column(Integer, nullable=True)
    size_x = Column(Integer, nullable=True)
    size_y = Column(Integer, nullable=True)
    owner = relationship("Customer", uselist=False)
    pickup = relationship("Location", uselist=False, foreign_keys=[pickup_location_id])
    dropoff = relationship("Location", uselist=False, foreign_keys=[dropoff_location_id])
    images = relationship(
        'Image',
        cascade="all, delete-orphan",
        single_parent=True
    )
