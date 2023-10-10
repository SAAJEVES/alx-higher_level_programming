#!/usr/bin/python3

'''function that creates an Object from a “JSON file”'''

import json

def load_from_json_file(filename):
    '''creates an object from a JSON file

    Args:
        filename: name of JSON file

    Returns:
        returns a python data structure
    '''
    with open(filename, mode='r', encoding='utf-8') as file:
        python_obj = json.load(file)
        return python_obj
