#!/usr/bin/python3
"""The module for rotating 2D Matrix"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    The matrix must be edited in-place.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for x in matrix:
        for j in range(n):
            x.reverse()
    return matrix
