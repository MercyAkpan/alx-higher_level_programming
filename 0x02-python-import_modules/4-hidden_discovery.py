#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allfiles = dir()
    for iter in range(len(allfiles)):
        if (allfiles[iter][-2:]) == "__":
            continue
        print("{}".format(allfiles[iter]))
