#!/usr/bin/python3

'''creation of is_same_class function'''


def is_same_class(obj, a_class):
    '''function that returns True if the object is 
    exactly an instance of the specified class ; otherwise False
    
    Args:
        obj: an instance of an object
        a_class: name of a class
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
