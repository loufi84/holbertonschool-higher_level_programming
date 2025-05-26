#!/usr/bin/python3
"""
Module 100-my_int
Defines a class MyInt that inherits from int but inverts == and != operations.
"""


class MyInt(int):
    """
    A subclass of int with inverted equality logic.

    This class behaves like an integer, but the equality and inequality
    operators are reversed. Any comparison using `==` will always return False,
    and using `!=` will always return True, regardless of the values involved.
    """

    def __eq__(self, other):
        """
        Override the equality operator (==).

        Returns:
            bool: Always returns False, regardless of the compared value.
        """
        return False

    def __ne__(self, other):
        """
        Override the inequality operator (!=).

        Returns:
            bool: Always returns True, regardless of the compared value.
        """
        return True
