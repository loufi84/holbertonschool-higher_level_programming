#!/usr/bin/python3
'''
A module for a class.
'''


class BaseGeometry:
    '''
    There is nothing to say here.
    '''
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Method to check if the value is an integer
        Args:
            value: Value to test.
            name: Name of the value.
        '''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    '''
    New class inheriting from BaseGeometry.
    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.
    '''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
