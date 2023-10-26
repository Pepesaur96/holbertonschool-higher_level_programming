#!/usr/bin/python3
"""Test module for base class"""

import os
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for base.py"""

    def test_init(self):
        """Test init method"""
        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_to_json_string(self):
        """Test to_json_string method"""
        dicts = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_str = Base.to_json_string(dicts)
        expected = json.dumps(dicts)
        self.assertEqual(json_str, expected)

    # def test_save_to_file(self):
    #     """Test save_to_file method"""
    #     filename = "Base.json"
    #     objs = [Base(1), Base(2)]
    #     Base.save_to_file(objs)
    #     with open(filename, 'r') as file:
    #         saved_objs = Base.from_json_string(file.read())
    #     self.assertEqual(objs, saved_objs)

    def test_from_json_string(self):
        """Test from_json_string method"""
        json_str = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        dicts = Base.from_json_string(json_str)
        expected = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        self.assertEqual(dicts, expected)

    # def test_create(self):
    #     """Test create method"""
    #     dictionary = {'id': 1, 'name': 'Alice'}
    #     obj = Base.create(**dictionary)
    #     self.assertEqual(obj.id, 1)

    # def test_load_from_file(self):
    #     """Test load_from_file method"""
    #     filename = "Base.json"
    #     with open(filename, 'w') as file:
    #         file.write(
    #             '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]')
    #     objs = Base.load_from_file()
    #     expected = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    #     self.assertEqual(objs[0].id, expected[0]['id'])
    #     self.assertEqual(objs[1].id, expected[1]['id'])


if __name__ == "__main__":
    unittest.main()
