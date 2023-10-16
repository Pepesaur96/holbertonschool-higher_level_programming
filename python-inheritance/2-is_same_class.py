#!/usr/bin/python3
"""
Defines a function that returns True if the object is exactly an instance of
the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_

    Returns:
        _type_: _description_
    """
    return type(obj) is a_class
