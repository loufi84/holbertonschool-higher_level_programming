#!/usr/bin/python3
"""
Module to print a name.
This module provides a single function that print a name in stdout.
"""


def say_my_name(first_name, last_name=""):
    """
    Print a name in stdout.
    Args:
        first_name: The first name of the person
        last_name: The last name of the person
    Raises:
        TypeError: If first_name or last_name aren't strings
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
