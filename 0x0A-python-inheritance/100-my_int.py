#!/usr/bin/bash

'''Create MyInt Class'''


class MyInt(int):
    '''Inherit from int'''

    def __init__(self, num):
        '''Initialization method'''
        self.num = num

    def __eq__(self, another):
        '''Magic Method Equal to'''
        if self.num == another:
            return False
        else:
            return True

    def __ne__(self, another):
        '''Magic Method Not Equal to'''
        if self.num != another:
            return False
        else:
            return True
