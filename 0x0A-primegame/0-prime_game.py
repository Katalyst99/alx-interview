#!/usr/bin/python3
"""The module for Prime Game"""


def isWinner(x, nums):
    """
    Function where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    """
    if x <= 0 or not nums:
        return None

    maxNum = max(nums)
    prime = [True] * (maxNum + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(maxNum ** 0.5) + 1):
        if prime[i]:
            for mult in range(i * i, maxNum + 1, i):
                prime[mult] = False

    mWins = 0
    bWins = 0

    for n in nums:
        if play(n, prime):
            mWins += 1
        else:
            bWins += 1
    if mWins < bWins:
        return "Ben"
    elif mWins > bWins:
        return "Maria"
    else:
        return None


def play(n, prime):
    """Function for simulating the game and determine winner."""
    moves = 0
    for number in range(2, n + 1):
        if prime[number]:
            moves += 1
    return moves % 2 == 1
