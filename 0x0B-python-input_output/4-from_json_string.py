#!/usr/bin/pyhton3

'''function that returns an object (Python data structure) represented by a JSON string'''
from io import StringIO
import json

def from_json_string(my_str):
    '''returns an object represented by a JSON string
    
    Args:
        my_str: json strinfs

    Returns:
        returns an object (python data structure)
    '''
    json_str = StringIO(my_str)
    python_str = json.load(json_str)
    return python_str
