#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = my_list.copy()
    if idx >= len(new_list) or idx < 0:
        return my_list
    else:
        del new_list[idx]
        return new_list
