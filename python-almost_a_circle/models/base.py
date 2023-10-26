#!/usr/bin/python3
""" Base class """


from os import path
import json


class Base:
    """ Base class
    Attributes:
        __nb_objects (int): number of objects
        id (int): id of object

    Methods:
        __init__(self, id=None)
        to_json_string(list_dictionaries)
        save_to_file(cls, list_objs)
        from_json_string(json_string)
        create(cls, **dictionary)
        load_from_file(cls)
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
        if list_dictionaries is None:
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

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string method """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create method """
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        elif cls.__name__ == "Square":
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ load_from_file method """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                objs = cls.from_json_string(f.read())
            return [cls.create(**obj) for obj in objs]
        except FileNotFoundError:
            return []

    @classmethod
    def to_dictionary(cls, obj):
        """To dictionary method"""
        attrs = ["id", "width", "height", "x", "y"]
        return {key: getattr(obj, key) for key in attrs}
