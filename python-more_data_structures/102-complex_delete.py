#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    else:
        for key, val in dict(a_dictionary).items():
            if val == value:
                del a_dictionary[key]
        return a_dictionary
