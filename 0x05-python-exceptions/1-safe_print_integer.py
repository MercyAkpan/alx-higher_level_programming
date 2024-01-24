#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
# that is  if one tries to print it as an integer and no err
# or occurs then, it returns True (not 1 and 0).
    except (TypeError, ValueError):
        return (False)
