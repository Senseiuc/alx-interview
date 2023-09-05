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
    numbs = [i for i in range(2, num + 1)]
    for i in numbs:
        is_prime = True
        for j in range(2, i // 2):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            numbs = [k for k in numbs if k % i != 0]
    return count


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
