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
    # Check for type
    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    m_a = np.array(m_a)
    m_b = np.array(m_b)

    return m_a @ m_b
