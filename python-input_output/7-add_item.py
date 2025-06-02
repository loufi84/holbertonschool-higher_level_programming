#!/usr/bin/python3
'''
This module provides a script that adds all arguments to a python list
and save them to a file
'''
import json
import sys
import os.path


def save_to_json_file(my_obj, filename):
    '''
    This function serialize an object and writes it into a file
    Args:
        my_obj: The object to serialize
        filename: The file to write to
    '''
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    '''
    This function open a file and creates an object from the JSON string
    Args:
        filename: The file to check
    '''
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


filename = "add_item.json"

if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
