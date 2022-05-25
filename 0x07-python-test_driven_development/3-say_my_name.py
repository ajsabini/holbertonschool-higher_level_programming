#!/usr/bin/python3
"""Module - print complete name"""


def say_my_name(first_name, last_name=""):
    """
        the function, recieve first and last
        name, control if they are string, and
        then  print complete name o show an error
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
