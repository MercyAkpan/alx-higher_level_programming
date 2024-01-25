#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two distinct lists element by element.

    Args:
        my_list_1 (list): The 1st list.
        my_list_2 (list): The 2nd list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for iter in range(list_length):
        try:
            div = my_list_1[iter] / my_list_2[iter]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
