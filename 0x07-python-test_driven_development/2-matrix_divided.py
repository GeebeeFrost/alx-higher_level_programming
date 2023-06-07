#!/usr/bin/python3
"""This module contains the implementatin of the matrix_divided function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number
    Args:
        matrix (list): matrix of numbers
        div (int or float): number to divide matrix numbers
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix is None or matrix == []:
        raise TypeError("matrix must be a matrix "
                        + "(list of lists) of integers/floats")
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix "
                            + "(list of lists) of integers/floats")
        row_length = len(matrix[0])
        if len(matrix[i]) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if (
                    not isinstance(matrix[i][j], int)
                    and not isinstance(matrix[i][j], float)):
                raise TypeError("matrix must be a matrix "
                                + "(list of lists) of integers/floats")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
