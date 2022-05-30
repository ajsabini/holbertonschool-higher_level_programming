#!/usr/in/python3
"""module - exactly class"""


def is_same_class(obj, a_class):
    """
        check if two objets are
        the same class
    """
    if type(obj) is a_class:
        ret = True
    else:
        ret = False

    return ret
