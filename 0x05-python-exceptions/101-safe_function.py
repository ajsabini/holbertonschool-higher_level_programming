#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    res = None
    try:
        res = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
    return res
