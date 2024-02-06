#!/usr/bin/python3
"""
Unit test module for State class
"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models.state import State


class TestState(unittest.TestCase):
    """
    Tests correct construction of State instances
    """

    def test_is_instance(self):
        test = State()
        self.assertIsInstance(test, State)

    def test_store(self):
        test = State()
        self.assertIn(test, models.storage.all().values())

    def test_unique_IDs(self):
        test1 = State()
        test2 = State()
        self.assertNotEqual(test1.id, test2.id)
