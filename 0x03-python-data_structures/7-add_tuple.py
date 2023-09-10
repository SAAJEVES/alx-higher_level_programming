#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    len_a = len(list_a)
    len_b = len(list_b)
    if len_a < 2:
        if len_a == 1:
            list_a = [list_a[0], 0]
        elif len_a == 0:
            list_a = [0, 0]
    if len_b < 2:
        if len_b == 1:
            list_b = [list_b[0], 0]
        elif len_b == 0:
            list_b = [0, 0]
    tuple_a = tuple(list_a)
    tuple_b = tuple(list_b)
    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    return (a, b)
