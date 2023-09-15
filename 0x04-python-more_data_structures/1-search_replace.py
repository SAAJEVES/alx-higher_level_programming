#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """This replaces any occurrence of a value in a list"""
    new_list = []
    for num in my_list:
        if num == search:
            new_list.append(replace)
            continue
        new_list.append(num)
    return new_list
