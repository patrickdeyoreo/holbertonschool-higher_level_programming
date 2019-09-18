#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    list(map(lambda row: print(*row, sep=', '), matrix))
