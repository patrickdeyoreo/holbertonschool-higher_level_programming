#!/usr/bin/python3
"""Provides a function to compute pascal triangles"""


def pascal_triangle(n):
    """Compute the pascal triangle of n"""
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if 0 < j < i:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            else:
                row.append(1)
        triangle.append(row)
    return triangle
