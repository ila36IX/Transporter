#!/usr/bin/python
"""
The images table
An image is row in table with image location info (URL or PATH)
"""
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Image(BaseModel, Base):
    """images table"""
    __tablename__ = 'images'
    img_path = Column(String(300))
    img_url = Column(String(300))
