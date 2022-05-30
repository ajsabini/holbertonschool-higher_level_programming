#!/usr/bin/python3
"""module - su class of"""


def inherits_from(obj, a_class):
    """
        function that return true, if
        objet is an instance of a class
        that inherited from spec class
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
