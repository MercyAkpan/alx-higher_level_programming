#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (1)
# that is  if one tries to print it as an integer and no err
# or occurs then, it returns 1 - True.
    except Exception:
        return (0)
