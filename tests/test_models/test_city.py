#!/usr/bin/python3
"""Unit test module for City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests correct construction of City instances"""
    def test_city_go(self):
        a_city = City()
        self.assertIsInstance(a_city, City())
        self.assertTrue(hasattr(a_city, "state_id"))
        self.assertTrue(hasattr(a_city, "name"))

    def test_city_gone(self):
        a_city = City()
        self.assertEqual(a_city.state_id, "")
        self.assertEqual(a_city.name, "")

if __name__ == '__main__':
    unittest.main()
