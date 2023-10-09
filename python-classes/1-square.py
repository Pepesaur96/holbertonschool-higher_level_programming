#!/usr/bin/python3
"""This module contains a class Square that defines a square by:
-Private instance attribute: size
-Instantiation with size (no type/value verification)
"""


class Square:
    """This class defines a square"""

    def __init__(self, size):
        """This method is the constructor and it takes in an argument called size"""
        self.__size = size
