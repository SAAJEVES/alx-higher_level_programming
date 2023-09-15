#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """This function returns the element(s) that is(are) not common"""
    set_3 = set_1 ^ set_2
    return set_3
