#!/usr/bin/python3
def number_keys(a_dictionary):
    res = 0
    list_ = list(a_dictionary.keys())

    for iter in list_:
        res = res + 1

    return (res)
