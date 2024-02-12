#!/usr/bin/python3
"""Unit test module for Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests correct construction of Amenity instances"""
    def test_amenity_declare(self):
        an_amenity = Amenity()
        self.assertTrue(hasattr(an_amenity, "name"))

    def test_amenity_attributes(self):
        an_amenity = Amenity()
        self.assertTrue(hasattr(an_amenity, "name"))
        self.assertEqual(an_amenity.name, "")
        an_amenity.name = "Skylight"
        self.assertEqual(an_amenity.name, "Skylight")

if __name__ == '__main__':
    unittest.main()
