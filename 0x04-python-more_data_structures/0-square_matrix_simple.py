#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """ Compute a new matrix with each element squared
    """
    if matrix is not None:
        return list(map(
            lambda row: list(map(
                lambda x: x ** 2, row
            )),
            matrix
        ))
    return None
