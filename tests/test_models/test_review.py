#!/usr/bin/python3
"""Unit test module for Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests correct construction of Review instances"""
    def test_review_init_eq(self):
        """unittest test test class"""
        a_review = Review()
        self.assertIsInstance(a_review, Review)
        self.assertTrue(hasattr(a_review, "place_id"))
        self.assertTrue(hasattr(a_review, "user_id"))
        self.assertTrue(hasattr(a_review, "text"))

    def test_review_attributes(self):
        a_review = Review()
        self.assertEqual(a_review.place_id, "")
        self.assertEqual(a_review.user_id, "")
        self.assertEqual(a_review.text, "")

if __name__ == '__main__':
    unittest.main()
