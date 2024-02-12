#!/usr/bin/python3
"""Module for Amenity class Unittests"""
import unittest
import models
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests correct construction of Amenity instances"""
    def test_is_instance(self):
        test = Amenity()
        self.assertIsInstance(test, Amenity)

    def test_store(self):
        test = Amenity()
        self.assertIn(test, models.storage.all().values())

    def test_unique_IDs(self):
        test1 = Amenity()
        test2 = Amenity()
        self.assertNotEqual(test1.id, test2.id)

if __name__ == '__main__':
    unittest.main()
