#!/usr/bin/python3
"""
Task 0: minimum operations
"""

"""
def minOperations(n):
    a method that calculates the fewest number
    of operations needed to result in exactly
    n H characters in the file

    if type(n) != int or n <= 0:
        return 0
    hCf = h_c_f(n)
    max_op = n // hCf
    while hCf != 1:
        x = h_c_f(hCf)
        max_op += hCf // x
        hCf = x
    return max_op


def h_c_f(val):

    calculates the highest common factor

    if val <= 3:
        return 1
    fac = 1
    for i in range(2, (val // 2) + 1):
        if (val % i) == 0:
            fac = i
    return fac
"""


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    # print('H', end='')
    while done < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = done
            done += clipboard
            ops_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif clipboard > 0:
            # paste
            done += clipboard
            ops_count += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return ops_count
