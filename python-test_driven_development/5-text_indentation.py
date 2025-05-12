#!/usr/bin/python3
"""
Module to print an indented text.
This module provides a single function that prints
a text with 2 new lines after each of these characters:
. ? and :
"""


def text_indentation(text):
    """
    Prints a text with indentation when meeting specific characters
    Args:
        text: The text to print
    Raises:
        TypeError: if the text is not a string
    """
    # Check if the text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    start = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[start:i+1].rstrip())
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            start = i
        else:
            i += 1

    if start < len(text):
        print(text[start:].rstrip(), end="")
