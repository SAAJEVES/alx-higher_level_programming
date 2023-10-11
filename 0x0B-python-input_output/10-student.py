#!/usr/bin/python3

'''Creates a Student Class'''

class Student:
    '''Students Class'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of a Student instance'''
        json_dict = {}

        if attrs == None:
            json_dict["first_name"] = self.first_name
            json_dict["last_name"] = self.last_name
            json_dict["age"] = self.age
            return json_dict
        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict
