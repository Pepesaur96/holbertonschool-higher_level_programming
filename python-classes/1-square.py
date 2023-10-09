#!/usr/bin/python3
"""This module contains a class Square that defines a square by:
-Private instance attribute: size
-Instantiation with size (no type/value verification)
"""


class Square:
    """This class defines a square"""

    def __init__(self, size):
        """Initializes an instance of the Square class
        Args:
            size (int): The size of the square"""
        self.__size = size
