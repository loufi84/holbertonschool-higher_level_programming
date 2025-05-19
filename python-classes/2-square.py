#!/usr/bin/python3
'''
This module provides a single class defining a square
'''


class Square:
    '''
    This class defines a square based on an attribute named size.
    Size must be an int and positive.
    Size is private to allow more control of square.

    Args:
        size (int): The size of the square, must be positive

    Attributes:
                size (int): The size of the square, must be positive
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
