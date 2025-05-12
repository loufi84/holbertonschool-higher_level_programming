#!/usr/bin/python3
"""
Module for matrix division.
This module provides a single function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    Args:
        matrix: The matrix to work with
        div: The nulber to divide matrix by
    Returns:
        A new matrix
    Raises:
        TypeError: If the matrix is not a list of integers or floats
        TyperError: If the rows are not the same size
        TypeError: If div is not a number (int or float)
        ZeroDivisionError: If div is equal to 0
    """
    # Check if matrix is a matrix
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    # Check if all values are numbers
    if not all(isinstance(e, (int, float)) for row in matrix for e in row):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    # Check if each rows are the same size
    row_length = len(matrix[0] if matrix else 0)
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create the new matrix and appends new numbers (originals by div)
    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(round(i / div, 2))
        new_matrix.append(new_row)

    return new_matrix
