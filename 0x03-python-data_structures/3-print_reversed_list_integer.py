#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # count = len(my_list) - 1
    for iter in my_list[::-1]:
        print("{}".format(iter))
