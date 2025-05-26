#!/usr/bin/python3
'''
This module defines a class that inherit from list.
'''


class MyList(list):
    '''
    A class that inherit from list and use a public method to
    print the list but sorted.
    '''
    def print_sorted(self):
        '''
        A method to print a sorted list.
        '''
        print(sorted(self))
