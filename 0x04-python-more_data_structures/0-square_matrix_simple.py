#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """This function modifies a two dimension list"""
    if len(matrix) == 0:
        reture None
    else:
        num = []
        for row in matrix:
            a = list(map(lambda x: x *x, row))
            num.append(a)
        return num
