#!/usr/bin/python3
"""Unit test module for State class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Tests correct construction of City instances"""
    def test_state_init_eq(self):
        """unittest test test class"""
        a_state = State()
        self.assertTrue(hasattr(a_state, 'name'))
        self.assertEqual(a_state.name, "")

if __name__ == '__main__':
    unittest.main()
