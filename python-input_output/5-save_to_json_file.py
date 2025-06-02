#!/usr/bin/python3
'''
This module provides a function that writes an object to a text file.
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    This function serialize an object and writes it into a file
    Args:
        my_obj: The object to serialize
        filename: The file to write to
    '''
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
