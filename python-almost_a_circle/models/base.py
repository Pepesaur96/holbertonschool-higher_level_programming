#!/usr/bin/python3
""" Base class """


class Base:
    """ Base class
    Attributes:
        __nb_objects (int): number of objects
        id (int): id of object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init method
        Args:
            id (int): id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
