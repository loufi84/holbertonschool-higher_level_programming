#!/usr/bin/python3
'''

'''
from functools import total_ordering


class MyInt(int):
    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
