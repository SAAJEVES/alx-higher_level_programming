#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = 0
    if idx >= len(my_list) or idx < 0:
        return my_list
    else:
        for num in my_list:
            if i == idx:
                my_list[idx] = element
                return my_list
            i += 1
