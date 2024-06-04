#!/usr/bin/python3
""" Making Change
    using dynamic programming
"""
import numpy as np


def makeChange(coins, total):
    """ making change function
    """
    if total <= 0:
        return 0

    arr = np.full(total + 1, np.inf)
    # arr = [inf, inf, inf, ..., inf] | len(arr) = total + 1
    arr[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            arr[i] = min(arr[i], arr[i - coin] + 1)
            if i == total:
                break

    return int(arr[total]) if arr[total] != np.inf else -1
