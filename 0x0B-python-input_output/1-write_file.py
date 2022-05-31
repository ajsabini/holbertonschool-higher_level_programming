#!/usr/bin/python3
"""
    write a strin to a utf-8 text file
    and return the num of character written
"""


def write_file(filename="", text=""):
    """function that recieves the filename and string"""
    with open(filename, mode='w', encoding="utf-8") as f:
        write_data = f.write(text)
        return write_data
