#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elements in a list

    Args:
        my_list (list): the type list to print
        x (int): the number of integers to print

    Returns:
        The number of elements printed
    """
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
    return num - 1

my_list = [1, 2, 3, 4, 5]
