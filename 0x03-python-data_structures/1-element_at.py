#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    if idx > len(my_list) or idx < 0:
        return None
    else:
        for num in my_list:
            if i == idx:
                return my_list[idx]
            i += 1
