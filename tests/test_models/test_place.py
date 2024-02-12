#!/usr/bin/python3
"""Unit test module for Place class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests correct construction of Place instances"""
    def test_place_declare(self):
        a_place = Place()
        self.assertTrue(hasattr(place, 'state_id'))
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'name'))

if __name__ == '__main__':
    unittest.main()
