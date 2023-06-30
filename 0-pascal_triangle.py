"""
A function that returns a pascal triangle of n
"""


def pascal_triangle(n):
    if n <= 0:
        return ([])
    p_list = [[1]]
    temp = []
    for i in range(n - 1):
        c_list = p_list[-1]
        temp.append(1)
        for i in range(len(c_list) - 1):
            temp.append(c_list[i] + c_list[i + 1])
        temp.append(1)
        p_list.append(temp)
        temp = []
    return (p_list)
