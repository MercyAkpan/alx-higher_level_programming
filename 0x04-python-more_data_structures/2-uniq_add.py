#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    number = 0

    for iter in new_list:
        number += iter

    return (number)
