#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""
    if matrix:
        for i in matrix:
            for j in i:
                print("{:d}".format(j),
                      end="{}".format(
                        "\n" if i[len(i) - 1] == j else " "))
