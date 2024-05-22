#!/usr/bin/python
"""
[images table]
An image row is represente image location info (URL or PATH)
Every image could be assigned to one of those:
    - Vehicle (which a driver is piloting 1->M)
    - Item (which a posted by customer to transport 1->M)
    - User (THis relation will be used to give profile picture 1->1)
"""
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Image(BaseModel, Base):
    """images table"""
    __tablename__ = 'images'
    img_path = Column(String(300))
    img_url = Column(String(300))
    item_id = Column(
        Integer,
        ForeignKey('items.id', name="fk_item_img"),
        nullable=True
    )
    vehcile_id = Column(
        Integer,
        ForeignKey('vehicles.id', name="fk_truck_img"),
        nullable=True
    )
