#!/usr/bin/python3

'''Creating Base Class'''

from json import dumps

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that converts to JSON object"""
        if list_dictionaries is None:
            return "[]"
        return dumps(list_dictionaries)

