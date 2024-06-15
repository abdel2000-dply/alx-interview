#!/usr/bin/python3
""" Prime Game
"""


def isPrime(n):
    """ prime numbers with Sieve of Eratosthenes algorithm
    """
    isPrime = [True for i in range(n + 1)]
    p = 2
    while p**2 <= n:
        if isPrime[p] is True:
            for i in range(p**2, n + 1, p):
                isPrime[i] = False
        p += 1
    isPrime[0] = isPrime[1] = False

    return isPrime


def isWinner(x, nums):
    """ Prime Game Winner
    """
    if x < 1 or nums is None:
        return None

    winner = {'Maria': 0, 'Ben': 0}
    max_num = max(nums)
    isPrimeNum = isPrime(max_num)
    prime_counts = [0] * (max_num + 1)

    # Calculate the number of primes up to each number
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if isPrimeNum[i] else 0)

    for n in nums:
        if prime_counts[n] % 2 == 1:
            winner['Maria'] += 1
        else:
            winner['Ben'] += 1

    if winner['Maria'] > winner['Ben']:
        return "Maria"
    elif winner['Maria'] < winner['Ben']:
        return "Ben"
    else:
        return None
