#!/usr/bin/env python3
"""
Task 0: minimum operations
"""

def minOperations(n):
    """
    a method that calculates the fewest number
    of operations needed to result in exactly
    n H characters in the file
    """
    hCf = h_c_f(n)
    max_op = n // hCf
    if hCf == 1:
        return n
    else:
        while hCf != 1:
            x = h_c_f(hCf)
            max_op += hCf // x
            hCf = x
    return max_op


def h_c_f(val):
    """
    calculates the highest common factor
    """
    if val <= 3:
        return 1
    fac = 1
    for i in range(2, (val // 2) + 1):
        if (val % i) == 0:
            fac = i
    return fac
