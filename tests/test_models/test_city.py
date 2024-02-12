#!/usr/bin/python3
"""Unit test module for City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Class test City"""
    def test_city(self):
        """unittest test test class"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

if __name__ == '__main__':
    unittest.main()
