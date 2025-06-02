#!/usr/bin/python3
'''
This module provides a function that append a new string after
a specific pattern.
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    This is the function to search for a specific string and add a
    specified line
    Args:
        filename: The file to search into
        search_string: The string to look after
        new_string: The string to append
    '''
    with open(filename, 'r') as f:
        lines = f.readlines()

    new_line = []
    for line in lines:
        new_line.append(line)
        if search_string in line:
            new_line.append(new_string)

    with open(filename, 'w') as f:
        f.writelines(new_line)
