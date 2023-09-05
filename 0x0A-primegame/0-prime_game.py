#!/usr/bin/python3
"""
0. Prime Game
"""


def prime_count(num):
    """
    Returns the number of prime factors
    """
    count = 0
    if num == 1:
        return count
    if num == 2:
        return 1
    is_prime = [True] * (num + 1)
    p = 2
    while p * p <= num:
        if is_prime[p]:
            for i in range(p * p, num + 1, p):
                is_prime[i] = False
        p += 1
    return len([i for i in range(2, num + 1) if is_prime[i]])


def isWinner(x, nums):
    """
    x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    """
    ben, jane = 0, 0
    for i in range(x):
        p_count = prime_count(nums[i])
        if p_count % 2 == 0:
            ben += 1
        else:
            jane += 1
    if ben > jane:
        return 'Ben'
    elif jane > ben:
        return 'Maria'
    return None
