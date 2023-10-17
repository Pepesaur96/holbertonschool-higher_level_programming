#!/usr/bin/python3
"""Module that returns an object (Python data structure) represented by a JSON
string"""


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a
    JSON string"""
    import json
    return json.loads(my_str)
