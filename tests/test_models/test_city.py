#!/usr/bin/python3
"""Unit test module for City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests correct construction of City instances"""
    def test_city_declare(self):
        self.a_city = City

    def test_city_input(self):
        self.assertEqual(self.a_city.name, "")

if __name__ == '__main__':
    unittest.main()
