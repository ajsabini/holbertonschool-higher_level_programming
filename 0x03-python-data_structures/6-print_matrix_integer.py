#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elements in row:
            print("{:d}".format(elements), end="")
            if (row.index(elements) + 1) < len(row):
                print(" ", end="")
        print("\n", end="")
