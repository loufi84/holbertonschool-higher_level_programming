#!/usr/bin/python3
"""
Module to multiply 2 matrices using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices using numpy's matmul
    function after validating the inputs.

    Args:
        m_a: First matrix (list of lists of integers or floats)
        m_b: Second matrix (list of lists of integers or floats)

    Returns:
        A new matrix resulting from the matrix multiplication.

    Raises:
        TypeError: If the input matrices are not
        lists of lists of integers or floats.
        ValueError: If the matrices cannot be multiplied
        due to dimension mismatch.
    """

    # Validate that m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    # Validate that m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Validate that m_a and m_b are not empty
    if len(m_a) == 0 or len(m_b) == 0 or len(m_a[0]) == 0 or len(m_b[0]) == 0:
        if len(m_a) == 0:
            raise ValueError("m_a can't be empty")
        else:
            raise ValueError("shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)")

    # Validate that each row in m_a and m_b is the same length
    row_length_a = len(m_a[0])
    row_length_b = len(m_b[0])
    if any(len(row) != row_length_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != row_length_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Validate that all elements in m_a and m_b are numbers
    if (any(not all(isinstance(val, (int, float))
                    for val in row) for row in m_a)):
        raise TypeError("m_a should contain only integers or floats")
    if (any(not all(isinstance(val, (int, float))
                    for val in row) for row in m_b)):
        raise TypeError("m_b should contain only integers or floats")

    # Validate matrix dimensions for multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication using np.matmul
    return np.matmul(m_a, m_b)
