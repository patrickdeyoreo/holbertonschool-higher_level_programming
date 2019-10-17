#!/usr/bin/python3
"""Provides a function to compute pascal triangles"""


def pascal_triangle(n):
    """Compute the pascal triangle of n"""
    triangle = []
    if n > 0:
        triangle.append([1])
        if n > 1:
            for i in range(1, n):
                row = [1]
                for j in range(1, i):
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
                row.append(1)
                triangle.append(row)
    return triangle
