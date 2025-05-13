#!/usr/bin/python3
"""
A module to multiply 2 matrices.
This module provides a single function that takes 2
matrices and multiply them
"""


def matrix_mul(m_a, m_b):
    """
    This function will multiply 2 matrices.
    Args:
        m_a: The first matrix
        m_b: The second matrix
    Raises:
        TypeError: If m_a or m_b aren't list or list of lists
        TypeError: If m_a or m_b contains an element not int or float
        TypeError: If m_a and m_b aren't of same size
        ValueError: If m_a or m_b are empty
        ValueError: If m_a and m_b can't be multiplied
    """
    # Check if matrices are list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if matrices are list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if matrices are empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Check if all values are int or float
    if not all(isinstance(e, (int, float)) for row in m_a for e in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(e, (int, float)) for row in m_b for e in row):
        raise TypeError("m_b should contain only integers or floats")

    # Check if m_a and m_b rows are same size
    rows_len_a = len(m_a[0] if m_a else 0)
    for row in m_a:
        if len(row) != rows_len_a:
            raise TypeError("each row of m_a must be of the same size")
    rows_len_b = len(m_b[0] if m_b else 0)
    for row in m_b:
        if len(row) != rows_len_b:
            raise TypeError("each row of m_b must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix result initialization with zeros
    res = [[0 for a in range(len(m_b[0]))] for a in range(len(m_a))]

    # Manual multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                res[i][j] += m_a[i][k] * m_b[k][j]

    return res
