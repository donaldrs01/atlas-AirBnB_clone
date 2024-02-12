#!/usr/bin/python3
"""Unit test module for State class"""
import unittest
from models.state import State

my_model = State()


class TestState(unittest.TestCase):
    """Tests correct construction of State instances"""
    def test_state(self):
        """unittest test test class"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

if __name__ == '__main__':
    unittest.main()
