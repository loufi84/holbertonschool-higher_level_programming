#!/usr/bin/python3
'''
A module for a class.
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        return self.__width * self.__height
