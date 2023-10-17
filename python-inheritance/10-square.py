#!/usr/bin/python3
"""Module 10-square
Contains class Square
inherits from Rectangle
Instantiation with size validated by integer_validator"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle
    Methods:
        __init__(self, size)
    """

    def __init__(self, size):
        """validate and initialize size
        Args:
            size (int): private
        """
        self.interger_validator("size", size)
        super().__init__(size, size)
        self.__size = size
