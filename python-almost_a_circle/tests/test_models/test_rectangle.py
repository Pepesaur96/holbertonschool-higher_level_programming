#!/usr/bin/python3

import os
import pep8
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models import rectangle
Rectangle = rectangle.Rectangle


class TestPep8(unittest.TestCase):
    """Pep8 class"""

    def test_pep8(self):
        """test for pep8"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ['models/rectangle.py', 'tests/test_models/test_rectangle.py']
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, "fix pep8")


class TestRectangle(unittest.TestCase):
    """Rectangle class tests"""

    def test_all_attr_given(self):
        """test if all attributes are given"""
        r1 = Rectangle(10, 2, 1, 9, 99)
        self.assertTrue(r1.width == 10)
        self.assertTrue(r1.height == 2)
        self.assertTrue(r1.x == 1)
        self.assertTrue(r1.y == 9)
        self.assertTrue(r1.id == 99)

    def test_no_attr_given(self):
        """test if no attributes are given"""
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_default_attr(self):
        """test if default attributes are given"""
        r1 = Rectangle(10, 2)
        self.assertTrue(r1.width == 10)
        self.assertTrue(r1.height == 2)
        self.assertTrue(r1.x == 0)
        self.assertTrue(r1.y == 0)
        self.assertTrue(r1.id == 1)

    def test_attr_validated(self):
        """test if attributes are validated"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("string", 2)
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "string")
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, "string")
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, -1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 1, "string")
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, 1, -1)

    def test_private_attr_access(self):
        """test if attributes are private"""
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_number_of_args(self):
        """test for too many arguments"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, 9, 99, 100)
        """test for too few arguments"""
        with self.assertRaises(TypeError):
            Rectangle(10)
            Rectangle()
            Rectangle(None)

    def test_class(self):
        """test for class is recctangle"""
        self.assertTrue(type(Rectangle(10, 2)) is Rectangle)

    def test_area(self):
        """test for area"""
        r1 = Rectangle(3, 2)
        self.assertTrue(r1.area() == 6)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertTrue(r2.area() == 56)

    def test_display(self):
        """test for display"""
        r1 = Rectangle(4, 6)
        f = StringIO()
        with redirect_stdout(f):
            r1.display()
        s = f.getvalue()
        self.assertEqual(s, "####\n####\n####\n####\n####\n####\n")

    def test_str(self):
        """test for __str__"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """test update"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update()
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update(99)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 10/10')
        r.update(99, 1)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 1/10')
        r.update(99, 1, 2)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 1/2')
        r.update(99, 1, 2, 3, 4)
        self.assertEqual(str(r), '[Rectangle] (99) 3/4 - 1/2')
        """Test invalid *args"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(99, 1, 2, 3, "string")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(99, 1, 2, 3, -99)
        """Test method: update(*kwargs)"""
        r.update(id=55)
        self.assertEqual(str(r), '[Rectangle] (55) 3/4 - 1/2')
        r.update(id=44, x=770, y=880, width=990)
        self.assertEqual(str(r), '[Rectangle] (44) 770/880 - 990/2')
        """Test mixture of valid and invalid *kwargs"""
        r.update(nokey=1000, invalid=2000, testing=3000, id=4000)
        self.assertEqual(str(r), '[Rectangle] (4000) 770/880 - 990/2')

    def test_to_dictionary(self):
        """test to_dictionary"""
        r = Rectangle(1, 2, 3, 4, 5)
        d = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(r.to_dictionary(), d)
        self.assertTrue(type(r.to_dictionary()) is dict)
