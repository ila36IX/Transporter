#!/usr/bin/python3
"""
This module defines a base class for all the other entities that will be
inheret from it
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import mapped_column 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    # id = Column(Integer, nullable=False, primary_key=True, unique=True)
    # The use of mapped_column is jsut to make the id always appear first
    id = mapped_column(Integer, nullable=False, primary_key=True, unique=True, sort_order=-1)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.to_dict())

    def save(self):
        """Updates updated_at with current time when instance is changed. Every
        instane that inherets from base_model should call this mothod in order
        to store it in db
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        # dictionary.update({'__class__':
        #                   (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        """usage: delete object"""
        from models import storage
        storage.delete(self)
        storage.save()
