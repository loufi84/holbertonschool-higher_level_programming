#!/usr/bin/python3
'''

'''


class CountedIterator():
    def __init__(self, iterable):
        self.__iterable = iter(iterable)
        self.__count = 0

    def __next__(self):
        item = next(self.__iterable)
        self.__count += 1
        return item

    def get_count(self):
        return self.__count
