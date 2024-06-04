#!/usr/bin/python3
""" Making Change
    using dynamic programming
"""


def makeChange(coins, total):
    """ making change function
    """
    if total <= 0:
        return 0

    arr = [float('inf')] * (total + 1)
    # arr = [inf, inf, inf, ..., inf] | len(arr) = total + 1
    arr[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            arr[i] = min(arr[i], arr[i - coin] + 1)

    return arr[total] if arr[total] != float('inf') else -1