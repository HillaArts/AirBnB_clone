#!/usr/bin/python3
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        # Test the initialization of a BaseModel instance
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertIsInstance(base_model.id, str)
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertTrue(hasattr(base_model, 'updated_at'))
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_save(self):
        # Test the save method
        base_model = BaseModel()
        original_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(original_updated_at, base_model.updated_at)

    def test_to_dict(self):
        # Test the to_dict method
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)
        self.assertIn('__class__', base_model_dict)

    def test_str(self):
        # Test the __str__ method
        base_model = BaseModel()
        str_representation = str(base_model)
        self.assertIsInstance(str_representation, str)
        self.assertIn(base_model.id, str_representation)
        self.assertIn(str(base_model.__dict__), str_representation)

    def test_kwargs_init(self):
        # Test initialization with kwargs
        data = {
            'id': 'test_id',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-02T12:00:00.000000',
            'custom_attribute': 'custom_value'
        }
        base_model = BaseModel(**data)
        self.assertEqual(base_model.id, 'test_id')
        self.assertEqual(base_model.custom_attribute, 'custom_value')
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()

