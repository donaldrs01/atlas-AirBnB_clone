#!/usr/bin/python3
"""Unittests for User class"""
import unittest
from models.user import User


class Test_User(unittest.TestCase):
    """unittests for user"""
    def test_user_attributes(self):
        """Unittests that test basic instantiation with various attributes"""
        user = User()

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

        user.email = "test@hotmail.com"
        user.password = "password123"
        user.first_name = "Joe"
        user.last_name = "Schmo"

        self.assertEqual(user.email, "test@hotmail.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "Joe")
        self.assertEqual(user.last_name, "Schmo")

if __name__ == '__main__':
    unittest.main()
