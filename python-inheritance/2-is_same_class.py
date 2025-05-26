#!/usr/bin/python3
'''
This module provides a function that check if an object is of
specified class.
'''


def is_same_class(obj, a_class):
    '''
    This method checks if an object is an instance of a class.
    Args:
        obj: The object to check.
        a_class: The class to compare.
    Returns:
            True if obj is of a_class, False if not.
    '''
    if type(obj) is a_class:
        return True
    return False
