#!/usr/bin/python3

'''Creating Base Class'''


class Base:
    '''A class called Base'''
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization Method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
