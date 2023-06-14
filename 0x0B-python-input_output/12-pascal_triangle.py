#!/usr/bin/python3
"""This module contains the pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle
    Args:
        n (int): limit
    """
    if n <= 0:
        return []
    result = [[1]]
    while len(result) != n:
        mid = result[-1]
        end = [1]
        for i in range(len(mid) - 1):
            end.append(mid[i] + mid[i + 1])
        end.append(1)
        result.append(end)
    return result
