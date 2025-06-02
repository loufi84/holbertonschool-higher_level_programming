#!/usr/bin/python3
'''
This module provides a function that returns the dictionary description
with simple data structure
'''


def class_to_json(obj):
    '''
    The function to return the dictionary description
    Args:
        obj: The object to check
    '''
    return obj.__dict__
