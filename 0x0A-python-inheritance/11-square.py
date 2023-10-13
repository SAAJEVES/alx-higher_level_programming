#!/usr/bin/python3

'''Creating A Square Class'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square that inherits from Rectangle'''

    def __init__(self, size):
        '''initialization method'''
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        '''Area of Square'''
        return self.__size * self.__size

    def __str__(self):
        '''Printed Object'''
        return f"[Square] {self.__size}/{self.__size}"
