"""
Unittest module for file_storage
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """
        Creates instance of FileStorage
        """
        self.instance = FileStorage()  # creates instance of FileStorage

    def test_new_method(self):
        """
        Test functionality of 'new' method that adds
        object to dictionary
        """
        test = BaseModel()  # create instance of BaseModel
        self.instance.new(test)  # call 'new' to add to directory

        key = f"{test.__class__.__name__}.{test.id}"
        self.assertIn(key, self.instance._FileStorage__objects)
        #  checks if key present in dictionary
        self.assertEqual(self.instance._FileStorage__objects[key], test)
        #  checks if key matches test instance
