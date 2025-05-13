#!/usr/bin/python3
"""
A module to multiply 2 matrices using
NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices using numpy
    Args:
        m_a: First matrix
        m_b: Second matrix
    Return:
        A new matrix
    Raises:
        NumPy exceptions
    """
    return np.matmul(m_a, m_b)
