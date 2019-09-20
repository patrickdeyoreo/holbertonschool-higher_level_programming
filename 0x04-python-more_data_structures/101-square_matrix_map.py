#!/usr/bin/python


def square_matrix_map(matrix=[]):
    """ Create a matrix a of the square of each element
    """
    if matrix is not None:
        return list(map(
            lambda row: list(map(
                lambda x: x ** 2, row
            )),
            matrix
        ))
    return None
