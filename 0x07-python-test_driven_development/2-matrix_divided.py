#!/usr/bin/python3
"""
A module of 2-matrix_divided
"""


def matrix_divided(matrix, div):
    """
    A function that divides a matrix by a given element


    Atrributes:
    matrix (list) - the matrix to be divided
    div (int) (float) - the divisor

    raises:
    TypeError - if matrix is not a list of lists
    TypeError - if div or element in matrix is not int or float
    ZeroDivisionError - if div is 0

    Returns:
    returns the new matrix consisting of quotients"""

    new_matrix = []
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    length_row = len(matrix[0])
    if not all(len(row) == length_row for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) '
                                'of integers/floats')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        new_row = []
        for value in row:
            quotient = round((value / div), 2)
            new_row.append(quotient)
        new_matrix.append(new_row)
    return new_matrix
