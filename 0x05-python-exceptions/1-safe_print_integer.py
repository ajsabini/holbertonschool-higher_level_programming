#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        ret = True
    except Exception:
        ret  = False
    return ret
