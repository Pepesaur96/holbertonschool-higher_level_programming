#!/usr/bin/python3
"""This module contains a class Square that defines a square by:
-Private instance attribute: size
-Instantiation with optional size
-Public instance method: def area(self)
-Public instance method: def size(self) to retrieve it
-Public instance method: def size(self, value) to set it
-Public instance method: def my_print(self) that prints the square with the
    character '#' to stdout
-Public instance method: def __str__(self) that returns a string representation
    of the square with the character '#'"""


class Square:
    """This class defines a square by private instance attributes 'size' and
    'position'.
    Args:
        size (int, optional): The size of the square. Defaults to 0.
        position (tuple, optional): The position of the square as a tuple of 2
        positive integers.
        Defaults to (0, 0).
    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class with optional size
        and position.
        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square as a tuple
            of 2 positive integers.
            Defaults to (0, 0).
        Raises:
            TypeError: If size is not an integer or position is not a tuple of
            2 positive integers.
            ValueError: If size is less than 0 or position values are less
            than 0."""
        self.size = size
        self.position = position

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for the 'position' attribute.
        Returns:
            tuple: The position of the square as a tuple of 2 positive
            integers."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for the 'position' attribute.
        Args:
            value (tuple): The new position value to set.
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If position values are less than 0."""
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate the area of the square.
        Returns:
            int: The area of the square."""
        return (self.__size) ** 2

    def my_print(self):
        """Print a square of '#' characters to stdout with the specified
        position.
        If size is equal to 0, print an empty line.
        Don't fill lines with spaces when position[1] > 0."""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                            for rows in range(self.__size)]))
