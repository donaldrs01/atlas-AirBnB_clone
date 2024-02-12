#!/usr/bin/python3
"""Unit test module for Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests correct construction of Review instances"""
    def test_review_declare(self):
        self.a_review = Review

    def test_review_input(self):
        self.assertEqual(self.a_review.name, "")

if __name__ == '__main__':
    unittest.main()
