#!/usr/bin/python
"""
The deliveries table
A delivery is a driver transporting/transported an item of a costumer
"""
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Enum, Time
from sqlalchemy.orm import relationship


class Delivery(BaseModel, Base):
    """Delivery table"""
    __tablename__ = 'deliveries'
    item_id = Column(
        Integer,
        ForeignKey('items.id', name="fk_delivery_item"),
        nullable=False
    )
    driver_id = Column(
        Integer,
        ForeignKey('drivers.id', name="fk_driver_item"),
        nullable=False
    )
    pickup_time = Column(Time, nullable=True)
    delivery_time = Column(Time, nullable=True)
    status = Column(
        Enum('pending', 'transiting', 'delivered', name='pending'),
        default="transiting"
    )
    item = relationship(
        "Item",
        backref="delivery",
        cascade="all, delete-orphan",
        uselist=False,
        single_parent=True
    )
