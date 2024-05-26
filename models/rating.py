#!/usr/bin/python
"""
The ratings table
Every rating is numeric openion of a user about a driver service 
"""
from models import *
import sqlalchemy
from sqlalchemy import Column, Text, ForeignKey, CheckConstraint
from sqlalchemy import Integer, SmallInteger
from sqlalchemy.orm import relationship


class Rating(BaseModel, Base):
    """ratings table"""
    __tablename__ = 'ratings'
    rating = Column(SmallInteger, CheckConstraint('rating >= 0 AND rating <= 5'), nullable=False)
    comment = Column(Text, nullable=True)
    rated_driver_id = Column(
        ForeignKey(
            'drivers.id',
            name="fk_driver_rate"
        ),
        nullable=False
    )
    rater_customer_id = Column(
        Integer,
        ForeignKey(
            'customers.id',
            name="fk_customer_rate",
        ),
        nullable=False
    )
