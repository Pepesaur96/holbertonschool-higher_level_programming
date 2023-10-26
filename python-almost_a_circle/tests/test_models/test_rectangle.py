#!/usr/bin/python3
"""unittest for rectangle.py"""

import unittest
import io
import unittest.mock
import json
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """unittest for rectangle.py"""

    def test_init(self):
        """test init method"""
        rectangle = Rectangle(5, 4, 2, 3, 7)
        self.assertEqual(rectangle.id, 7)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

    def test_width_and_height_properties(self):
        """test width and height properties"""
        rectangle = Rectangle(4, 3)
        rectangle.width = 6
        rectangle.height = 7
        self.assertEqual(rectangle.width, 6)
        self.assertEqual(rectangle.height, 7)
        with self.assertRaises(ValueError):
            rectangle.width = 0
        with self.assertRaises(TypeError):
            rectangle.width = "invalid"

    def test_x_and_y_properties(self):
        """test x and y properties"""
        rectangle = Rectangle(2, 2)
        rectangle.x = 3
        rectangle.y = 4
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)
        with self.assertRaises(ValueError):
            rectangle.x = -1
        with self.assertRaises(TypeError):
            rectangle.x = "invalid"

    def test_area(self):
        """test area method"""
        rectangle = Rectangle(4, 3)
        self.assertEqual(rectangle.area(), 12)

    def test_str(self):
        """test str method"""
        rectangle = Rectangle(3, 4, 1, 2, 5)
        self.assertEqual(str(rectangle), "[Rectangle] (5) 1/2 - 3/4")

    def test_update(self):
        """test update method"""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update(6, 7, 8, 9, 10)
        self.assertEqual(rectangle.id, 6)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 8)
        self.assertEqual(rectangle.x, 9)
        self.assertEqual(rectangle.y, 10)

    def test_to_dictionary(self):
        """test to_dictionary method"""
        rectangle = Rectangle(2, 3, 4, 5, 6)
        rectangle_dict = rectangle.to_dictionary()
        expected = {'id': 6, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        self.assertEqual(rectangle_dict, expected)


if __name__ == "__main__":
    unittest.main()
