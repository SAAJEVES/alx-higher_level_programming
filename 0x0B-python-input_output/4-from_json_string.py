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
    python_str = json.load(my_str)
    return python_str
