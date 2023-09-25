#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
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

