#!/usr/bin/python3
"""square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class
    Import from models/rectangle.py
    Attributes:
        size (int): size of square
        x (int): x coordinate of square
        y (int): y coordinate of square
        id (int): id of square
    Methods:
        __init__(self, size, x=0, y=0, id=None)
        size(self)              size(self, value)
        area(self)
        display(self)
        __str__(self)
        update(self, *args, **kwargs)"""

    def __init__(self, size, x=0, y=0, id=None):
        """init method
        Private instance attributes:
            size (int): size of square
            x (int): x coordinate of square
            y (int): y coordinate of square
        """
        super().__init__(size, size, x=0, y=0, id=None)
        self.size = size

    @property
    def size(self):
        """size getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter method"""
        self.width = value
        self.height = value

    def __str__(self):
        """str method"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id,
                                             self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """update method"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
