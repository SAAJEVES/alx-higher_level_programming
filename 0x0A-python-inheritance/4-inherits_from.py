#!/usr/bin/python3

'''create inherits_from function'''


def inherits_from(obj, a_class):
    '''
    function that returns True if the object is
    an instance of a class that inherited (directly or indirectly)
    from the specified class; otherwise False

    Args:
        obj: object
        a_class: class
    '''
    obj_class = type(obj)
    return issubclass(obj_class, a_class)
