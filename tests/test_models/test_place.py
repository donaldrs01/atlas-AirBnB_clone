#!/usr/bin/python3
"""Unit test module for Place class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests correct construction of Place instances"""
    def test_place_declared(self):
        a_place = Place()
        self.assertIsInstance(a_place, Place())
        self.assertTrue(hasattr(a_place, "city_id"))
        self.assertTrue(hasattr(a_place, "user_id"))
        self.assertTrue(hasattr(a_place, "name"))
        self.assertTrue(hasattr(a_place, "description"))

    def test_variable_gone(self):
        a_place = Place()
        self.assertEqual(a_place.city_id, "")
        self.assertEqual(a_place.user_id, "")
        self.assertEqual(a_place.name, "")
        self.assertEqual(a_place.description, "")
        self.assertEqual(a_place.number_rooms, 0)
        self.assertEqual(a_place.number_bathrooms, 0)
        self.assertEqual(a_place.max_guest, 0)
        self.assertEqual(a_place.price_by_night, 0)
        self.assertEqual(a_place.latitude, 0.0)
        self.assertEqual(a_place.longitude, 0.0)
