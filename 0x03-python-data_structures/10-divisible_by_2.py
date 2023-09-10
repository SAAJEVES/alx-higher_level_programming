#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = []
    for num in my_list:
        a.append(bool(num % 2))
    return a
