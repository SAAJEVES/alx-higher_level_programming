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

    new_list = []
    for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            value = 0
            print("divison by 0")
        except TypeError:
            value = 0
            print("wrong type")
        except IndexError:
            value = 0
            print("out of range")
        finally:
            new_list.append(value)
    return new_list
