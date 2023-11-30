#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    length_row = len(matrix[0])
    if not all(len(row) == length_row for row in matrix):
            raise TypeError('Each row of the matrix must have the same size')
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

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
