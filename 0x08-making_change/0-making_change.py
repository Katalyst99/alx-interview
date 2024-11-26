#!/usr/bin/python3
"""The module for the coin change problem"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    change = 0
    for c in coins:
        if total == 0:
            break
        keep = total // c
        change += keep
        total %= c

    return change if total == 0 else -1
