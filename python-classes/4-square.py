#!/usr/bin/python3
"""This module contains a class Square that defines a square by:
-Private instance attribute: size
-Instantiation with optional size
-Public instance method: def area(self)
-Public instance method: def size(self) to retrieve it
-Public instance method: def size(self, value) to set it"""


class Square:
    """This class defines a square by a private instance attribute 'size'.
    Args:
        size (int, optional): The size of the square. Defaults to 0.
    Attributes:
        __size (int): The size of the square."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class with an
        optional size.
        Args:
            size (int, optional): The size of the square. Defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0."""
        self.__size = size

    @property
    def size(self):
        """Getter method for the 'size' attribute.
        Returns:
            int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the 'size' attribute.
        Args:
            value (int): The new size value to set.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.
        Returns:
            int: The area of the square."""
        return self.__size ** 2
