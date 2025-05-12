#!/usr/bin/python3
"""
Module for add_integer function.
This module provides a single function that adds two integers.
Both inputs must be integers or float and are casted to integers
"""
def add_integer(a, b=98):
    """
    Adds two integers or float (casted ton integer)

    Args:
        a: First number (int or float)
        b: Second number (int or float), defaults to 98

    Returns:
        The sum of a and b as an integer

    Raises:
        TypeError: If a or b is not an integer or a float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
