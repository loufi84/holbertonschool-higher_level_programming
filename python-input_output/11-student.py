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

    def to_json(self, attrs=None):
        '''
        The function to return the dictionary description of Student
        '''
        if isinstance(attrs, list):
            for element in attrs:
                if not isinstance(element, str):
                    return self.__dict__
            filtered = {}
            for key in attrs:
                if key in self.__dict__:
                    filtered[key] = self.__dict__[key]
            return filtered
        return self.__dict__

    def reload_from_json(self, json):
        for key in json:
            setattr(self, key, json[key])
