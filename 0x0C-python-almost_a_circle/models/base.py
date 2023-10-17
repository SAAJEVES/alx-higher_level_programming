#!/usr/bin/python3

'''Creating Base Class'''

import json


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        python_list = json.loads(json_string)

        if len(python_list) == 0 or python_list is None:
            return []
        return python_list

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        class_name = cls.__name__
        filename = f"{class_name}.json"
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, 'w') as file:
            file.write(json_string)
