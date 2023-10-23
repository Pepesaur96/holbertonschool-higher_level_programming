#!/usr/bin/python3
""" Base class """


import json
import csv


class Base:
    """ Base class
    Attributes:
        __nb_objects (int): number of objects
        id (int): id of object

    Methods:
        __init__(self, id=None)
        to_json_string(list_dictionaries)
        save_to_file(cls, list_objs)
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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string method """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file method """
        objs = []
        if list_objs is not None:
            for obj in list_objs:
                objs.append(cls.to_dictionary(obj))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))
