#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    if n <= 0:
        return [[]]

    possibilities = []
    options = ["rock", "paper", "scissors"]

    def helper(roundElem, roundNumber):
        for i in range(0, len(options)):
            roundElem.append(options[i])
            if roundNumber == n:
                possibilities.append(roundElem.copy())
            else:
                helper(roundElem, roundNumber + 1)

            roundElem.pop()

    # Each element is an array containing n amount of elements
    helper([], 1)
    return possibilities


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")

