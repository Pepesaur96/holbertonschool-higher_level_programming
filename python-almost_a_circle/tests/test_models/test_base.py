#!/usr/bin/python3
"""Unittest for base.py"""

import unittest
import pep8
import json
import os
from models.base import Base
from models.rectangle import Rectangle


class TestPep8(unittest.TestCase):
    """Pep8 class"""

    def test_pep8(self):
        """test for pep8"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ['models/base.py', 'tests/test_models/test_base.py']
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, "fix pep8")


class TestBase(unittest.TestCase):
    """Base class tests"""

    def setUp(self):
        """test setup"""
        pass

    def tearDown(self):
        """test tear down"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_id(self):
        """test if id matches"""
        self.assertTrue(Base(999), self.id == 999)
        self.assertTrue(Base(0), self.id == 1)
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(-80), self.id == -80)

    def test_id_not_given(self):
        """test if id increments if passed none"""
        self.assertTrue(Base().id == 1)
        self.assertTrue(Base().id == 2)

    def test_id_string(self):
        """test if id is string"""
        self.assertTrue(Base("string").id == "string")

    def test_private_attr_access(self):
        """test if attributes are private"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    def test_invalid_args(self):
        """test for invalid arguments"""
        with self.assertRaises(TypeError):
            Base(50, 50)

    def test_class(self):
        """test for class"""
        self.assertTrue(type(Base()) is Base)

    def test_to_json_string(self):
        """test for to_json_string"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), "[{\"id\": 12}]")
        self.assertTrue(type(Base.to_json_string([{'id': 12}])) is str)

    def test_from_json_string(self):
        """test for from_json_string"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string("[{\"id\": 12}]"),
                         [{'id': 12}])
        self.assertTrue(type(Base.from_json_string("[]")) is list)

    def test_create(self):
        """test for create"""
        r1 = Rectangle(3, 5, 1, 2, 99)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), '[Rectangle] (99) 1/2 - 3/5')
        self.assertEqual(str(r2), '[Rectangle] (99) 1/2 - 3/5')
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_save_to_file(self):
        """test for save_to_file"""
        r1 = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 106)
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 2)

    def test_save_none_to_file(self):
        """test for save none to file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 2)

    def test_empty_to_none_to_file(self):
        """test for empty to none to file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 2)

    def test_load_from_file(self):
        """test for load from file"""
        r1 = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_input = Rectangle.load_from_file()
        self.assertTrue(type(list_rectangles_input) is list)
        self.assertTrue(type(list_rectangles_input[0]) is Rectangle)
        self.assertEqual(
            str(list_rectangles_input[0]), '[Rectangle] (99) 2/8 - 10/7')
        self.assertEqual(
            str(list_rectangles_input[1]), '[Rectangle] (98) 2/2 - 2/4')

    def test_load_from_file_none(self):
        """test for load from file none"""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_empty_fiel(self):
        """test for load from empty file"""
        open("Rectangle.json", "w").close()
        self.assertEqual(Rectangle.load_from_file(), [])
