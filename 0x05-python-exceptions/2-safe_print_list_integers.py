#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers.

    Args:
        my_list (list): contains list of elements to print
        x (int): number of elements to print

    Returns:
        prints the number of integers that were printed
    """

    num = 0
    for i in range(x):
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                num += 1
        except (TypeError, ValueError):
            continue
    print()
    return num
