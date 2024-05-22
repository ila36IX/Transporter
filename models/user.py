#!/usr/bin/python3
"""Represets users table
User is represniting an account info that the driver and customer need to
identify them selfs
 - A user could have a profile picture
"""
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from hashlib import md5
from sqlalchemy import Column, String, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import event


class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    phone = Column(String(128), nullable=True)
    birthday = Column(Date, nullable=True)
    img_id = Column(
        Integer, 
        ForeignKey('images.id', name="fk_user_img"),
        nullable=True
    )
    image = relationship("Image", uselist=False, cascade="all, delete-orphan", single_parent=True)


def hash5(target, value, oldvalue, initiator):
    """Hach the password using md5 algorithm
    This precedure function that will be invoked where set new value to
    password event is triggered
    """
    return md5(value.encode()).hexdigest()

event.listen(User.password, 'set', hash5, retval=True)
