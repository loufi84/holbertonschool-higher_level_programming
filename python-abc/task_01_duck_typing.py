#!/usr/bin/python3
"""Module that implements Shape, Circle and Rectangle for duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle shape with radius."""
    def __init__(self, radius):
        self.__radius = abs(radius)

    def area(self):
        return  math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2  * math.pi * self.__radius


class Rectangle(Shape):
    """Rectangle shape with width and height."""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Print area and perimeter of the given shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
