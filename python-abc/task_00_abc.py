#!/usr/bin/python3
'''
This module defines an abstract class Animal.
'''
from abc import ABC, abstractmethod


class Animal(ABC):
    '''
    Mother class abstract to define sub classes.
    '''
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    '''
    Class Dog that inherit from the abstract class Animal.
    '''
    def sound(self):
        return "Bark"


class Cat(Animal):
    '''
    Class Cat that inherit from the abstract class Animal.
    '''
    def sound(self):
        return "Meow"
