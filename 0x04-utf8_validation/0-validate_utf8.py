#!/usr/bin/python3
"""The module for UTF-8 Validation"""


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid UTF-8
    """
    nbytes = 0

    for by in data:

        if 128 <= by <= 191:

            if nbytes == 0:
                return False
            nbytes -= 1
        else:
            if nbytes > 0:
                return False

            if by >> 5 == 0b110:
                nbytes = 1
            elif by >> 4 == 0b1110:
                nbytes = 2
            elif by >> 3 == 0b11110:
                nbytes = 3
            elif by >> 7 == 0:
                nbytes = 0
            else:
                return False
    return nbytes == 0
