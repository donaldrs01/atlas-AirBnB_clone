#!/usr/bin/python3
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def instance_creation_blank(self):
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertIsNotNone(b.id)
        self.assertIsNotNone(b.created_at)
        self.assertIsNotNone(b.updated_at)

    def instance_creation_with_args(self):
        
