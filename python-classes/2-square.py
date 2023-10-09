#!/usr/bin/python3
"""This module contains a class Square that defines a square by:
-Private instance attribute: size
-Instantiation with size (no type/value verification)"""


class Square:
    """This class defines a square by a private instance attribute 'size'.

    Args:
        size (int, optional): The size of the square. Defaults to 0.

    Attributes:
        __size (int): The size of the square."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class with an optional
        size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
