import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        pass

    def test_instance_construct_blank(self):
        """Tests instance construction with no args"""
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertIsNotNone(b.id)
        self.assertIsNotNone(b.created_at)
        self.assertIsNotNone(b.updated_at)

    def test_instance_creation_with_args(self):
        """Tests instance construction with provided args"""
        timestamp = datetime.today().isoformat()  # converts to string
        custom_id = 75
        
        b = BaseModel(
            id = custom_id,
            created_at = timestamp,
            updated_at = timestamp
        )

        self.assertEqual(b.id, 75)
        self.assertEqual(b.created_at.isoformat(), timestamp)
        self.assertEqual(b.updated_at.isoformat(), timestamp)

    def test_save(self):
        """Tests save functionality by comparing timestamps"""
        b = BaseModel()
        current_datetime = datetime.now()
        b.save()
        self.assertGreaterEqual(b.updated_at, current_datetime)

    def test_to_dict(self):
        """Tests converting instance into dictionary values"""
        test = BaseModel()
        test_dictionary = test.to_dict()
        self.assertEqual(test_dictionary['__class__'], 'BaseModel')
        self.assertEqual(test_dictionary['id'], test.id)

    def test_str(self):
        b = BaseModel()
        self.assertTrue(str(b))
