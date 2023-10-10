#!/usr/bin/python3

'''function that writes an Object to a text file, using a JSON representation'''

import json

def save_to_json_file(my_obj, filename):
    '''writes an object to a text file, using a JSON representation
    
    Args:
        my_object: python object
        filename: name of text file

    Returns:
        Nothing
    '''
    json_obj = json.dumps(my_obj)
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json_obj)
