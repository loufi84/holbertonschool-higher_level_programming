#!/usr/bin/python3
'''
This module provides a method that check if an object is an instance
of a class or a class that inherited from.
'''


def is_kind_of_class(obj, a_class):
    '''
    This method check if the object is an instance.
    Args:
        obj: The object to check.
        a_class: The class to compare.
    Return:
            True if is an instance, False if not.
    '''
    if isinstance(obj, a_class):
        return True
    return False
