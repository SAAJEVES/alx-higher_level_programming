#!/usr/bin/python3

'''function that adds a new attribute to an object if it’s possible'''


def add_attribute(obj, attr, val):
    '''Raise a TypeError exception, with the message
    can't add new attribute if the object can’t 
    have new attribute'''
    if hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, val)
