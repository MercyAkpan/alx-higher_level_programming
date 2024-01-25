#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ = list(a_dictionary.keys())
    list_.sort()
    for iter in list_:
        print("{}: {}".format(iter, a_dictionary.get(iter)))
