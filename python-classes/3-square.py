#!/usr/bin/python3
"""This module contains a class Square that defines a square by:
-Private instance attribute: size
-Instantiation with optional size
-Public instance method: def area(self)"""


class Square:
    """This class defines a square by a private instance attribute 'size',
    and a public instance method 'def area(self)'"""

    def __init__(self, size=0):
        """Initializes a new Square instance with an optional size.
        Args:
            size (int, optional): The size of the new square instance.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square.
        Returns:
            The area of the square."""
        return self.__size ** 2
