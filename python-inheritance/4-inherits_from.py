#!/usr/bin/python3
'''
A module the provides a method to check if the object is an instance of a
class that inherited (directly or indirectly) from the specified class.
'''


def inherits_from(obj, a_class):
    '''
    The method that checks the inheritance.
    Args:
        obj: The object to check.
        a_class: The class to compare.
    Return:
            True if is a subclass, False if not.
    '''
    return issubclass(type(obj), a_class) and type(obj) is not a_class
