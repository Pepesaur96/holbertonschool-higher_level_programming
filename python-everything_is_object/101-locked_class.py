#!/usr/bin/python3
"""
LockedClass - prevents the user from dynamically creating new instance
attributes, except if the new instance attribute is called first_name
"""


class LockedClass:
    """
    __slots__ - is used to explicitly declare data members and
    deny the user to create any other attribute other than the ones
    specified
    """
    __slots__ = "first_name"
