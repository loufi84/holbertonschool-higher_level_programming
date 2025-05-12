#!/usr/bin/python3
"""
Module to print a square.
This module provides a single function that prints a square in stdout
"""


def print_square(size):
    """
    Print a square in stdout.
    Args:
        size: The length of the square
    Raises:
        TypeError: If size is not an integer
        TypeError: If size is float and less than 0
        ValueError: If size is less than 0
    """
    # Check if size is a float and < 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Check if size is not an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is < 0
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
