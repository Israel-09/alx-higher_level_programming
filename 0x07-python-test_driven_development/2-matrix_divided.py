#!/usr/bin/python3
"""
module contains a function that divides the
elements of a square matix.

example:
    >>> matrix = [[2, 6, 4], [2, 12, 8]]
    >>> div = 2
    >>> new = matrix_divided(matrix, div)
    >>> new
    [[1.0, 3.0, 2.0], [1.0, 6.0, 4.0]]
"""


def matrix_divided(matrix, div):
    """matrix_divided divides the element of matrix
    by the divisor, div.

    Args:
        matrix (list): the matrix to be maniputlated(divided).
        div (int, float): the divisor

    Raises:
        TypeError:  if matrix is not a list of list of type int/float
                    if the size of each row of the matrix is different
                    if div is not of type int/float

        ZeroDivisionError: if div is equal 0

    Returns:
        The return value. New matrix of the divided elements
    """
    m_error = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) is not list or matrix == []:
        raise TypeError(m_error)
    for row in matrix:
        if type(row) is not list or row == []:
            raise TypeError(m_error)
        else:
            for i in row:
                if type(i) is not int and type(i) is not float:
                    raise TypeError(m_error)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) is not row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
