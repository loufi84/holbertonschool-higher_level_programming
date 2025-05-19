#!/usr/bin/python3
'''
This module provides a single class defining a square.
'''


class Square:
    '''
    This class defines a square based on its size.
    Size must be an integer and positive.

    Args:
        size (int): The size of the square, must be positive

    Attribute:
                size (int): The size of the square, must be positive
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
        This method will calculate the area of the square
        based on the formula : area = size^2
        '''
        area = self.__size**2
        return area
