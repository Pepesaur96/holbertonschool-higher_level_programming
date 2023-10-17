#!/usr/bin/python3
"""Contains Student class"""


class Student():
    """Student class
    attributes:
        first_name (str): Student's first name.
        Last_name (str): Student's last name.
        age (int): Student's age.
    methods:
        to_json: returns dictionary representation of a Student instance
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic
