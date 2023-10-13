#!/usr/bin/python3

'''Create MyInt Class'''


class MyInt(int):
    '''Inherit from int'''

    def __init__(self, num):
        '''Initialization method'''
        self.num = num

    def __eq__(self, another):
        '''Magic Method Equal to'''
        return not super().__eq__(another)

    def __ne__(self, another):
        '''Magic Method Not Equal to'''
        return not super().__ne__(another)
