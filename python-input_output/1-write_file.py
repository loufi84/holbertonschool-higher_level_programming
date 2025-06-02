#!/usr/bin/python3
'''
This module provides a single function that writes a string to a text file.
'''


def write_file(filename="", text=""):
    '''
    This function writes a string to a text file, if it doesn't exist create it
    Args:
        filename: The file to write to
        text: The string to write
    '''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
