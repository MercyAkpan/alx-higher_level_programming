#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        maxi = my_list[0]
    for iter in range(len(my_list)):
        if my_list[iter] > maxi:
            maxi = my_list[iter]
    return maxi
