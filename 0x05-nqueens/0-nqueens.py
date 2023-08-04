#!/usr/bin/python3
"""
Task 0: N queens
Author: SenseiUC
"""
import sys

argv = sys.argv
if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
if not argv[1].isdigit():
    print("N must be a number")
    exit(1)
num = int(argv[1])
if num < 4:
    print('N must be at least 4')
    exit(1)


def check_if_attacking(positions, pos):
    """
    Check if a position is in attacking mode
    """
    cant_pick = []
    can_pick = []
    for i in positions:
        x, y = i[0] - pos[0], i[1] - pos[1]
        if i[0] == pos[0] or i[1] == pos[1] or abs(x) == abs(y):
            cant_pick += [i]
        else:
            can_pick += [i]
    return cant_pick, can_pick


def n_queens(n: int):
    """
    A function that prints the number of ways
    queens can be arranged in a non attacking way
    """
    all_pos = [[x, y] for x in range(n) for y in range(n)]
    get_all_possible(0, all_pos, [], n)


def get_all_possible(index, can_pick, picked, n):
    """
    Gets all possible combinations
    """
    if not can_pick:
        if len(picked) == n:
            print(picked)
        return
    index_does_not_exist = True
    for i in can_pick:
        if i[0] == index:
            index_does_not_exist = False
            can_pick_cp = can_pick[:]
            picked_cp = picked[:]
            x, y = check_if_attacking(can_pick_cp, i)
            can_pick_cp = y
            picked_cp += [i]
            get_all_possible(index + 1, can_pick_cp, picked_cp, n)
    if index_does_not_exist:
        return


if __name__ == '__main__':
    n_queens(num)
