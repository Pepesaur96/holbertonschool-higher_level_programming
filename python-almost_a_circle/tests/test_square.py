#!/usr/bin/python3
"""unittest for square.py"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """unittest for square.py"""

    def test_init(self):
        """test init method"""
        square = Square(5, 2, 3, 7)
        self.assertEqual(square.id, 7)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_size_property(self):
        """test size property"""
        square = Square(3)
        square.size = 6
        self.assertEqual(square.size, 6)
        with self.assertRaises(ValueError):
            square.size = -1
        with self.assertRaises(TypeError):
            square.size = "invalid"

    def test_area(self):
        """test area method"""
        square = Square(4)
        self.assertEqual(square.area(), 16)

    def test_str(self):
        """test str method"""
        square = Square(3, 1, 2, 5)
        self.assertEqual(str(square), "[Square] (5) 1/2 - 3")

    def test_update(self):
        """test update method"""
        square = Square(1, 2, 3, 4)
        square.update(5, 6, 7, 8)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_to_dictionary(self):
        """test to_dictionary method"""
        square = Square(2, 2, 2, 2)
        square_dict = square.to_dictionary()
        expected = {'id': 2, 'size': 2, 'x': 2, 'y': 2}
        self.assertEqual(square_dict, expected)


if __name__ == "__main__":
    unittest.main()
