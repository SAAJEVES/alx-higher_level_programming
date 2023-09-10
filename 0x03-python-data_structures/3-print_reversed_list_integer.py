#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = my_list[::-1]
    for num in a:
        print("{:d}".format(num))
