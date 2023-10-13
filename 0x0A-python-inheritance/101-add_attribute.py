#!/usr/bin/python3

'''function that adds a new attribute to an object if it’s possible'''


def add_attribute(obj, attr, val):
    '''Raise a TypeError exception, with the message
    can't add new attribute if the object can’t 
    have new attribute'''
    if isinstance(obj, str) or isinstance(obj, tuple) or isinstance(obj, int):
        raise TypeError("can't add new attribute")
    elif isinstance(obj, dict) or isinstance(obj, list) or isinstance(obj, set):
        raise TypeError("can't add new attribute")
    elif hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, val)
