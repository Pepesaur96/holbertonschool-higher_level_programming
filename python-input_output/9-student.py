#!/usr/bin/python3
"""Contains Student class"""


class Student:
    """Student class
    methods:
        to_json: returns dictionary representation of a Student instance
    """

    def __init__(self, first_name, Last_name, age):
        """Initializes a new Student.
        Args:
            first_name (str): Student's first name.
            Last_name (str): Student's last name.
            age (int): Student's age.
        Attributes:
            first_name (str): Student's first name.
            Last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.Last_name = Last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
