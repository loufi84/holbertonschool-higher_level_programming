#!/usr/bin/python3
'''
This module provides a single function reading a file with "with"
'''


def read_file(filename=""):
    '''
    This is the function reading file using "with"
    Args:
        filename: The file to open
    '''
    with open(filename, encoding="utf-8") as f:
        print(f.read())
