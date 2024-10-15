#!/usr/bin/python3
"""Algorithm: Minimum Operations"""


def minOperations(n):
    """
    A method that calculates the fewest number of operations,
    needed to result in exactly n H characters in the file.
    """
    div = 2
    numOps = 0

    if n <= 1:
        return 0

    while n > 1:
        if n % div == 0:
            n = n / div
            numOps += div
        else:
            div += 1
    return numOps
