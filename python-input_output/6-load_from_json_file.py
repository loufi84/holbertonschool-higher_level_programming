#!/usr/bin/python3
'''
This module provides a function that creates an object from a JSON
'''
import json


def load_from_json_file(filename):
    '''
    This function open a file and creates an object from the JSON string
    Args:
        filename: The file to check
    '''
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
