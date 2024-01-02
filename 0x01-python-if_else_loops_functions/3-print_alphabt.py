#!/usr/bin/python3
for ASCII_ALPHA in range (97, 123):
    if ASCII_ALPHA in [101, 113]:
	    continue;
    print("{}".format(chr(ASCII_ALPHA)), end='')
