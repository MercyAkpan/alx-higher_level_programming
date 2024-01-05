#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        new = []
        for iter in my_list:
            if iter % 2 == 0:
                new.append(True)
            else:
                new.append(False)
        return new
    return my_list
