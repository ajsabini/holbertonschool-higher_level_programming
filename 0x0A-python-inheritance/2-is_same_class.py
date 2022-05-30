#!/usr/in/python3
"""module - exactly class"""


def is_same_class(obj, a_class):
    """
        check if two objets are
        the same class
    """
    ret = type(obj) is a_class

    return ret
