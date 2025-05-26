#!/usr/bin/python3
'''

'''
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    '''
    
    '''
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    '''
    
    '''
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return (self.__radius**2) * math.pi

    def perimeter(self):
        return (2 * self.__radius) * math.pi

class Rectangle(Shape):
    '''
    
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

circle = Circle(5)
rectangle = Rectangle(4, 7)
shape_info(circle)
shape_info(rectangle)