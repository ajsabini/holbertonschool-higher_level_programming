#!/usr/bin/python3
"""Module - print a square"""


def print_square(size):
    """the function that print a quare,
    recieve the size, control if is an int
    and > 0, then print the square, or
    shown an error
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
