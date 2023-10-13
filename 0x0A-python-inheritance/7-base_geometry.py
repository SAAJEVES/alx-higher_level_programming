#!/usr/bin/python3

'''creating BaseGeometry class'''


class BaseGeometry:
    '''BaseGeometry Class'''

    def area(self):
        '''aread method'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates if integer'''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
