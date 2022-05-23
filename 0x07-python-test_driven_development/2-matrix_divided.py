#!/usr/bin/python3
"""Module - diide int/floats elements for a matrix"""


def matrix_divided(matrix, div):
    """the funtion"""
    cont = 0
    for x in matrix:
        cont += 1
        for y in x:
            if type(y) is not int and type(y) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    print(f"45 {x} el x")
    print(f"{cont} el cont")
    

