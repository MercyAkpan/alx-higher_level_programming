#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = len(argv) - 1
    if count == 0:
        print("0 arguments.")
    if count == 1:
        print("1 argument:")
    if count > 1:
        print(f"{count} arguments:")
    if count >= 1:
        for iter in range(1, count + 1):
            print("{}: {}".format(iter, argv[iter]))
