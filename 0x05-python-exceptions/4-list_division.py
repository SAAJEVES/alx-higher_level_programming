#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """function that divides element by element 2 lists

    Args:
        my_list_1 (list): first list
        my_list_2 (list): second list
        list_length (int): length of the returned list

    Returns:
        the new list with it corresponding division
    """
    value = 0
    new_list = []
        for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            value = 0
        except TypeError:
            print("wrong type")
            value = 0
        except IndexError:
            print("out of range")
            value = 0
        finally:
            new_list.append(value)
    return new_list
