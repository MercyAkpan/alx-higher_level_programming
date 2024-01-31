#!/usr/bin/python3
def increment(n):
    n += 1
    return(n) # I added a return fn to be the object 'b' points to.
a = 2
# I use the b to have a new object to point to.
b = increment(a)
print(b)
