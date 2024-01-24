def safe_print_list(my_list=[], x=0):
    actualen = 0
    for iter in range(x):
        try:
            print("{}".format(my_list[iter]), end="")
            actualen += 1
        except:
            break
    print("")
    return (actualen)
