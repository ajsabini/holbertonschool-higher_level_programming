#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    value = 0
    for x in range(len(matrix)):
        new_matrix.append([])
        for y in range(len(matrix[x])):
            ints = matrix[x][y] * matrix[x][y]
            new_matrix[x].append(ints)

    return new_matrix

