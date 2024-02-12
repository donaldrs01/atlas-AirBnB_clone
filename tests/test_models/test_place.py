#!/usr/bin/python3
"""Unit test module for Place class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests correct construction of Place instances"""
    def test_place_declare(self):
        self.a_place = Place

    def test_place_input(self):
        self.assertEqual(self.a_place.name, "")

if __name__ == '__main__':
    unittest.main()
