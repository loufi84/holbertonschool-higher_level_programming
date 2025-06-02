#!/usr/bin/python3
'''
This module provides a function that returns an object based on a JSON.
'''
import json


def from_json_string(my_str):
    '''
    This function returns an object based on a JSON string
    Args:
        my_str: The JSON string
    '''
    return json.loads(my_str, encoding="utf-8")
