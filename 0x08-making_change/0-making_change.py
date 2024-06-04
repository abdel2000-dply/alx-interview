#!/usr/bin/python3
""" Making Change
    using greedy algorithm
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            return count
        count += total // coin
        total %= coin

    if total != 0:
        return -1

    return count
