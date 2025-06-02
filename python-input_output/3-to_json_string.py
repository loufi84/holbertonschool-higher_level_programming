#!/usr/bin/python3
'''
This module provides a function that serialize an object into JSON
'''
import json


def to_json_string(my_obj):
    '''
    This function return a serialized object in JSON
    Args:
        my_obj: The object to serialize
    '''
    return json.dumps(my_obj)
