#!/usr/bin/python3
a = 89
b = 10
# c = a # c= 89
# a = b # a = 10 
# b = a # b = 89
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
