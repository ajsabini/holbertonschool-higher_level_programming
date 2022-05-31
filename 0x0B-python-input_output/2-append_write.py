#!/usr/bin/python3
"""
    append a string at the endo of an utf-8 text file
    and return number of characters added
"""


def append_write(filename="", text=""):
    """"""
    with open(filename, mode='a', encoding="utf-8") as f
        write_data = f.write(text)
        return write_data
