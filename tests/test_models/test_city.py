#!/usr/bin/python3
"""
Test the city ORM
"""
from models import *
import unittest

class TestCityDocs(unittest.TestCase):
    """Tests for the city ORM
    """
    def setUp(self):
        self.c = City(name="city1")
        self.l1 = Location(name="city1_location1")
        self.l2 = Location(name="city1_location2")
        self.l3 = Location(name="city1_location3")
        self.c.locations.append(self.l1)
        self.c.locations.append(self.l2)
        self.c.locations.append(self.l3)
        self.l1.save()
        self.l2.save()
        self.l3.save()
        self.c.save()
        self.id = self.c.id
        
    def test_create_city(self):
        """Test created city is exist in db"""
        c = storage.get("City", id=self.c.id)
        self.assertEqual(c.id, self.c.id)

    def test_location_related(self):
        """New city is related to locations"""
        c = storage.get("City", id=self.c.id)
        self.assertEqual(len(c.locations), 3)
        self.assertIn(self.l1, self.c.locations)
        
    def test_cascade_delete(self):
        """Deleteing city will cause delete all its related locations"""
        c = storage.get("City", id=self.c.id)
        id = c.locations[0].id
        c.delete()
        c = storage.get("Location", id=id)
        self.assertIsNone(c)
