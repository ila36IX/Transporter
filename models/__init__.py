#!/usr/bin/python3
"""
initialize the models package
"""
from models.city import City
from models.location import Location
from models.image import Image
from models.user import User
from models.customer import Customer
from models.vehicle import Vehicle
from models.driver import Driver
from models.item import Item
from models.delivery import Delivery
from models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()

classes = {
    "City" : City,
    "Image" : Image,
    "Location": Location,
    "User": User,
    "Customer": Customer,
    "Vehicle": Vehicle,
    "Driver": Driver,
    "Item": Item,
    "Delivery": Delivery
}

__all__ = [
    'City', 
    'Image',
    'Location',
    'User',
    'Customer',
    'Vehicle',
    'Driver',
    'Item',
    'Delivery',
    'storage',
    'classes'
]
