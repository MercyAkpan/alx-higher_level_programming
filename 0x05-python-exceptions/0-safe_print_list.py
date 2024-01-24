#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    actualen = 0
# couunt for indexe in string.
    for iter in range(x):
        try:
            print("{}".format(my_list[iter]), end="")
            actualen += 1
# for loop to print all elemenst in string
        except Exception:
            break
# except all Exception, for any exception encountered
    print("")
    return (actualen)
