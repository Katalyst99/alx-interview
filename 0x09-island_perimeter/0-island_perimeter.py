#!/usr/bin/python3
"""The module for Island Perimeter"""


def island_perimeter(grid):
    """Returns he perimeter of the island described in grid"""
    perim = 0
    x = len(grid)
    y = len(grid[0]) if x > 0 else 0

    for i in range(x):
        for j in range(y):
            if grid[i][j] == 1:
                perim += 4
                if j > 0 and grid[i][j - 1] == 1:
                    perim -= 2
                if i > 0 and grid[i - 1][j] == 1:
                    perim -= 2
    return perim
