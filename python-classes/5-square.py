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

    @property
    def size(self):
        '''
        This method is a property getter that return the private
        size attribute.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        This method is a setter that modifies the size of the square.

        Args:
            value (int): The new size of the square, must be positive
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):

        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)
