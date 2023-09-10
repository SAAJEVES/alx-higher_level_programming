#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list = my_list[::-1]
    if my_list:
        for num in my_list:
            print("{:d}".format(num))
    else:
        print("{}".format(my_list))
