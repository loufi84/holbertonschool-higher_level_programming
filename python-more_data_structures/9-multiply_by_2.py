#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = a_dictionary.copy()
    for key in a_dictionary:
        res[key] = a_dictionary.get(key) * 2
    return res
