#!/usr/bin/python3
"""Unit test module for City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Class test City"""
    def test_city_work(self):
        """unittest test test class"""
        a_city = City()
        self.assertTrue(hasattr(a_city, 'state_id'))
        self.assertTrue(hasattr(a_city, 'name'))

if __name__ == '__main__':
    unittest.main()
