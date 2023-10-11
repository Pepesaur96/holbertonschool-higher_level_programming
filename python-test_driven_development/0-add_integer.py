#!/usr/bin/python3
""" Module that adds two integers """


def add_integer(a, b=98):
    """ Function that adds two integers
    Args:
        a: first integer
        b: second integer
    Returns:
        The addition of a and b
    Raises:
        TypeError: If a or b are not integers or floats
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
