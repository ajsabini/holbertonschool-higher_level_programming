#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    uno = (0, 0)
    dos = (0, 0)
    if len(tuple_a) == 0:
        uno = 0, 0
    elif len(tuple_a) == 1:
        uno = tuple_a[0], 0
    else:
        uno = tuple_a[0], tuple_a[1]

    if len(tuple_b) == 0:
        dos = 0, 0
    elif len(tuple_b) == 1:
        dos = tuple_b[0], 0
    else:
        dos = tuple_b[0], tuple_b[1]

    return (uno[0] + dos[0], uno[1], dos[1])
