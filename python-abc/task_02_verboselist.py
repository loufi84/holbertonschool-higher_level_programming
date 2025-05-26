#!/usr/bin/python3
'''

'''
from abc import ABC, abstractmethod


class VerboseList(list):
    def append(self, object):
        print("Added [{}] to the list.".format(object))
        return super().append(object)

    def extend(self, iterable):
        print("Extended the list with [{}] items".format(len(iterable)))
        return super().extend(iterable)

    def remove(self, value):
        print("Removed [{}] from the list.".format(value))
        return super().remove(value)

    def pop(self, index=-1):
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
