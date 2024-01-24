#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0
    for count in range(0, x):
        try:
            print("{:d}".format(my_list[count]), end="")
            length += 1
# learn on different kinds of errors
        except (ValueError, TypeError):
            continue
    print("")
    return (length)
