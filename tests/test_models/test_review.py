#!/usr/bin/python3
"""Module for Review class Unittests"""
import unittest
import models
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests correct construction of Review instances"""
    def test_is_instance(self):
        test = Review()
        self.assertIsInstance(test, Review)

    def test_store(self):
        test = Review()
        self.assertIn(test, models.storage.all().values())

    def test_unique_IDs(self):
        test1 = Review()
        test2 = Review()
        self.assertNotEqual(test1.id, test2.id)

if __name__ == '__main__':
    unittest.main()
