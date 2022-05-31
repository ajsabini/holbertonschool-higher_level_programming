#!/usr/bin/python3
"""function that reds a UTF8 text and print in stdout"""


def read_file(filename=""):
    """
        the function, recieves filename
        and print it
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
