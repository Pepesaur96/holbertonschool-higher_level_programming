#!/usr/bin/python3
"""Class that inherits from list"""


class Mylist(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Function that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
