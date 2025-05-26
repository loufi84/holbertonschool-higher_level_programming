#!/usr/bin/python3
'''
This module provides a method that adds a new attribute to an object
if possible, based on the __dict__.
'''


def add_attribute(obj, name, value):
    '''
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to modify.
        name (str): The name of the new attribute.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object cannot accept new attributes.
    '''
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
