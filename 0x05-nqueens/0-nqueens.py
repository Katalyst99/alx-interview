#!/usr/bin/python3
"The module for solving N queens problem."""
import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)
if not sys.argv[1].isdigit():
    print('N must be a number')
    sys.exit(1)
if int(sys.argv[1]) < 4:
    print('N must be at least 4')
    sys.exit(1)
n = int(sys.argv[1])


def solveNqueens(n):
    """Program that solves the N queens problem."""
    solutions = []
    board = [-1] * n

    def backtrack(x):
        """Fucntion to implement backtracking"""
        if x == n:
            solutions.append([[i, board[i]] for i in range(n)])
        else:
            for y in range(n):
                if isValid(x, y):
                    board[x] = y
                    backtrack(x + 1)
                    board[x] = -1

    def isValid(x, y):
        """To check validity of each move"""
        for i in range(x):
            if board[i] == y or \
               board[i] - i == y - x or \
               board[i] + i == y + x:
                return False
        return True

    backtrack(0)
    return solutions


def solve(n):
    """Main function to print each solution"""
    solutions = solveNqueens(n)
    for sol in solutions:
        print(sol)


solve(n)
