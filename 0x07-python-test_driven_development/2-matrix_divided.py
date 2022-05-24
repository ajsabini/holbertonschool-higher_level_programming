#!/usr/bin/python3
"""Module - diide int/floats elements for a matrix"""


def matrix_divided(matrix, div):
    """the function"""
    newMatrix = []
    errorIntFl = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None:
        raise TypeError(errorIntFl)
    if type(matrix) is not list:
        raise TypeError(errorIntFl)
    if matrix == []:
        raise TypeError(errorIntFl)
    for x in matrix:
        if type(x) is not list:
            raise TypeError(errorIntFl)
        for y in x:
            if type(y) is not int and type(y) is not float:
                raise TypeError(errorIntFl)
    lenA = len(matrix[0])
    for x in matrix:
        if len(x) != lenA:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    newMatrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return newMatrix
