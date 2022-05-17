#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elems = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elems = elems + 1
        except ValueError:
            print("", end="")
        except TypeError:
            print("", end="")
    print()
    return elems

