#!/usr/bin/python3
"""Unit test module for State class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests correct construction of State instances"""
    def test_state_declare(self):
        self.a_state = State

    def test_state_input(self):
        self.assertEqual(self.a_state.name, "")

if __name__ == '__main__':
    unittest.main()
