#!/usr/bin/python3
"""Unit test module for Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests correct construction of Amenity instances"""
    def test_amenity_declare(self):
        self.a_amenity = Amenity

    def test_amenity_input(self):
        self.assertEqual(self.a_amenity.name, "")

if __name__ == '__main__':
    unittest.main()
