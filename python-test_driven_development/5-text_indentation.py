#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of these
    characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == " " and text[i - 1] in [".", "?", ":"]:
            continue
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
