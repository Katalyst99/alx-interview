#!/usr/bin/python3
"""Algorithm: Lockboxes"""


def canUnlockAll(boxes):
    """A method that determines if all the boxes can be opened."""
    allBoxes = len(boxes)
    keys = [0]
    unlocked = [False] * allBoxes
    unlocked[0] = True
    while keys:
        aBox = keys.pop()
        for key in boxes[aBox]:
            if key < allBoxes and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
