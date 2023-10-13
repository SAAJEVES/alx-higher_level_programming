#!/usr/bin/python3

'''Creating a Reactangle class'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class inheriting from BaseGeometry class'''

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        '''Area of Rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''Printed Rectangle Class'''
        return f"[Rectangle] {self.__width}/{self.__height}"
