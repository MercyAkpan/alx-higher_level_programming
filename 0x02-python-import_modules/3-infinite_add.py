#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv)
    initsum = 0
    for i in range(1, count):
        initsum += int(argv[i])
    print(initsum)
# i.e 0 + argv(1) + argv(2)... if argv is total of 4 args == ./command 1 2 3
#        0     1 2 3
# it would add argv(1) + argv(2) + argv(3)  = 6
# why is line 7 and 8 wrong ,if i did :
# count + 1 and argv[i + 1] respectively
