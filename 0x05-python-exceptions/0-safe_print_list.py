#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list == []:
        return None
    num = 0
    for val in my_list:
        try:
            print(val, end="")
            num += 1
        except:
            continue
        if num == x:
            break;
    print()
    return my_list[num - 1]

my_list = [1, 2, 3, 4, 5]
