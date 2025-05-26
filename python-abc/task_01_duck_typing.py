#!/usr/bin/python3
'''
Module that implement 3 classes to test duck typing.
'''
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    '''
    The abstract class mother of all.
    '''
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    '''
    Circle class inherits from Shape.
    Args:
        radius: The radius of the circle.
    '''
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return (self.__radius**2) * math.pi

    def perimeter(self):
        return (2 * self.__radius) * math.pi


class Rectangle(Shape):
    '''
    Rectangle class inherits from Shape.
    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.
    '''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__height + self.__width) * 2


def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
