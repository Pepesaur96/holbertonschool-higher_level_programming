#!/usr/bin/python3
"""
Defines a function that returns True if the object is an instance of, or if the
object is an instance of a class that inherited from, the specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class; otherwise
    False.
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
