#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    d = idx
    if d < 0:
        return my_list
    if d > len(my_list) - 1:
        return my_list
    else:
        my_list[d] = element
    return my_list
