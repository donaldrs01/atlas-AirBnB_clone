#!/usr/bin/python3
"""Module for City class Unittests"""
import unittest
import models
from models.city import City


class TestCity(unittest.TestCase):
    """Tests correct construction of City instances"""
    def test_is_instance(self):
        test = City()
        self.assertIsInstance(test, City)

    def test_store(self):
        test = City()
        self.assertIn(test, models.storage.all().values())

    def test_unique_IDs(self):
        test1 = City()
        test2 = City()
        self.assertNotEqual(test1.id, test2.id)

if __name__ == '__main__':
    unittest.main()
