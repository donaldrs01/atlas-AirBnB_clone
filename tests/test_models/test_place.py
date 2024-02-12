#!/usr/bin/python3
"""Module for Place class Unittests"""
import unittest
import models
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests correct construction of Place instances"""
    def test_is_instance(self):
        test = Place()
        self.assertIsInstance(test, Place)

    def test_store(self):
        test = Place()
        self.assertIn(test, models.storage.all().values())

    def test_unique_IDs(self):
        test1 = Place()
        test2 = Place()
        self.assertNotEqual(test1.id, test2.id)

if __name__ == '__main__':
    unittest.main()
