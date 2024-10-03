#!/usr/bin/python3
""" 
Algorithm:Pascal’s triangle
"""


def pascal_triangle(n):
    """
    A function that returns a list of lists of integers representing
    the Pascal’s triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for x in range(1, n):
        line = [1]
        for y in range(1, x):
            line.append(triangle[x-1][y-1] + triangle[x-1][y])
        line.append(1)
        triangle.append(line)

    return triangle
