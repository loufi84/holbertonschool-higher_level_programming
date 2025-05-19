#!/usr/bin/python3
'''
This module provides a simple class defining a rectangle.
'''


class Rectangle:
    '''
    This class will create an object rectangle.

    Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle

    Attributes:
                width (int): The width of the rectangle
                height (int): The height of the rectangle
    '''
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''
        A getter that returns the private attribute width.
        '''
        return self.__width

    @property
    def height(self):
        '''
        A getter that returns the private attribute height.
        '''
        return self.__height

    @width.setter
    def width(self, value):
        '''
        A setter to modify the private attribute width.

        Args:
            value (int): The value to replace rectangle's width.
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        '''
        A setter to modify the private attribute height.

        Args:
            value (int): The value to replace rectangle's height.
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
