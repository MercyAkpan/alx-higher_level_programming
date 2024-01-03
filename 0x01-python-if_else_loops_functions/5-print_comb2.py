#!/usr/bin/python3
for numbers in range(0, 100):
    if numbers in [99]:
        print("{:02d}".format(numbers), end='\n')
# one could put precision with the string itself with ""
# not with '' and not within .format()
        continue
    print("{:02d}".format(numbers), end=', ')
