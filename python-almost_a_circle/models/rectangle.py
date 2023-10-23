#!/usr/bin/python3
""" Rectangle class """

from models.base import Base


class Rectangle(Base):
    """ Rectangle class
    Import from models/base.py
    Attributes:
        __width (int): width of rectangle
        __height (int): height of rectangle
        __x (int): x coordinate of rectangle
        __y (int): y coordinate of rectangle
        id (int): id of rectangle
    Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        width(self)             width(self, value)
        height(self)            height(self, value)
        x(self)                 x(self, value)
        y(self)                 y(self, value)
        area(self)
        display(self)
        __str__(self)
        update(self, *args, **kwargs)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init method
        Private instance attributes:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x coordinate of rectangle
            y (int): y coordinate of rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter method"""
        return self.__width

    @property
    def height(self):
        """Height getter method"""
        return self.__height

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @width.setter
    def width(self, value):
        """Width setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Height setter method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter method"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter method"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area method"""
        return self.__width * self.__height

    def display(self):
        """Display method"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update method"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
