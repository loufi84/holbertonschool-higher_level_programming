#!/usr/bin/python3
'''
This module provides a class that defines a student
'''


class Student:
    '''
    This class defines a student.
    Args:
        first_name: student's first name
        last_name: student's last_name
        age: student's age
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        The function to return the dictionary description of Student
        '''
        return self.__dict__
