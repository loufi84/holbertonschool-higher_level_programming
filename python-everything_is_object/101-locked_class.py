#!/usr/bin/python3
class LockedClass:
    """
    This class will prevent user to dynamically create new instance attributes
    excpet if the new instance attribute is called first_name
    """
    __slots__ = ['first_name']
