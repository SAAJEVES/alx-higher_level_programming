#!/usr/bin/python3

'''a function that returns the JSON representation of an object (string)'''
import json


def to_json_string(my_obj):
    '''returns the JSON representation of an object

    Args:
        my_obj: python object

    Returns:
        returns a JSON representation
    '''
    json_string = json.dumps(my_obj)
    return json_string
