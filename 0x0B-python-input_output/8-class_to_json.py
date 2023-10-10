#!/usr/bin/python3

'''function that returns the dictionary 
description with simple data structure
(list, dictionary, string, integer and boolean) 
for JSON serialization of an object
'''

def class_to_json(obj):
    '''Returns a dictionary

    Args:
        obj: an instance of a class

    Returns:
        returns a dictionary distribution
    '''
    if not isinstance(obj, type(obj)):
        raise ValueError("Obj should be an instance of a class")

    obj_attr = vars(obj)

    json_dict = {}

    for key, value in obj_attr.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return json_dict
