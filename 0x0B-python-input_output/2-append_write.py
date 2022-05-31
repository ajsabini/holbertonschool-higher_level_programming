#!/usr/bin/python3
"""
    append a string at the endo of an utf-8 text file
    and return number of characters added
"""


def append_write(filename="", text=""):
    """function to append string to atext, recieve the fn and str"""
    with open(filename, mode="a", encoding="utf-8") as f:
        write_data = f.write(text)
        return write_data
