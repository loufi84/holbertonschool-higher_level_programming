#!/usr/bin/python3
'''
This module provides a class defining a simple square
'''


class Square:
    '''
    This class defines a square based on it's private attribute
    size. Size is private to ensure better control of the square.

    Args:
        size: The size of the square

    Attributes:
                size: The size of the square
    '''
    def __init__(self, size):
        self.__size = size
