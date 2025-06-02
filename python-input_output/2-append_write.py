#!/usr/bin/python3
'''
This module provides a function that appends a string to a file.
'''


def append_write(filename="", text=""):
    '''
    This function appends a string to a file.
    Args:
        filename: The file to append the text to
        text: The text to append
    '''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
