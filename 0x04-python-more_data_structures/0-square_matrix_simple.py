#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers in a matrix"""
    sqr_mat = [[x ** 2 for x in row] for row in matrix]
    return sqr_mat
