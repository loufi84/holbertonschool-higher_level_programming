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

    def __str__(self):
        '''
        This method will prints the rectangle.
        '''
        if self.__height == 0 or self.__width == 0:
            print()
            return
        line = "#" * self.__width
        rect = "\n".join([line for i in range(self.__height)])
        return rect
    
    def __repr__(self):
        '''
        This method is the official format for debugging object.
        '''
        return f"Rectangle({self.__width}, {self.__height})"

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

    def area(self):
        '''
        A public method that calculate the area of the rectangle.
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''
        A public method that calculate the perimeter of the rectangle.
        '''
        if self.__height == 0 or self.__width == 0:
            return 0

        return (self.__height + self.__width) * 2
