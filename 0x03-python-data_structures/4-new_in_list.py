#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp = my_list[:]
    d = idx
    if d < 0:
        return tmp
    if d > len(tmp) - 1:
        return tmp
    else:
        tmp[d] = element
    return tmp
