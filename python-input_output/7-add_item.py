#!/usr/bin/python3
"""Module that adds all arguments to a Python list, and then save them to a
file"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if FileNotFoundError:
    existing_content = []
else:
    existing_content = load_from_json_file(filename)

save_to_json_file(existing_content + argv[1:], filename)
