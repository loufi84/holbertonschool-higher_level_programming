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
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if (
            not isinstance(position, tuple) or
            len(position) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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
            value (int): The new size of the square, must be positive.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        '''
        This method is a property setter that returns the private
        position attribute.
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        This method is a setter that modifies the position
        of the square.

        Args:
            value (tuple): The new position of the square.
        '''
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        '''
        This method will calculate the area of the square
        based on the formula : area = size^2
        '''
        return self.__size**2

    def my_print(self):
        '''
        This method print a square using "#" characters, considering the
        position. If size is 0, prints an empty line.
        '''
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
