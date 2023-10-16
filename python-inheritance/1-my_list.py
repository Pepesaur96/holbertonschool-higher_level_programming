#!/usr/bin/python3
"""Class that inherits from list
arguments: list"""


class Mylist(list):
    """Class that inherits from list
    methods:
        print_sorted(self)"""

    def print_sorted(self):
        """Function that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
