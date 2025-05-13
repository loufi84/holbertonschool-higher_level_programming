#!/usr/bin/python3
"""
Module to multiply 2 matrices using NumPy
"""
import numpy as np
import sys


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
    # Check for types
    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    # Check for empty lists
    if not m_a or m_a == [[]]:
        raise ValueError("shapes (1,0) and (2,2) not aligned: 0"
                         " (dim 1) != 2 (dim 0)")
    if not m_b or m_b == [[]]:
        raise ValueError("shapes (2,2) and (1,0) not aligned: 2"
                         " (dim 1) != 1 (dim 0)")

    # Check dimensions before numpy conversion
    if len(m_a[0]) != len(m_b):
        a_shape = f"({len(m_a)},{len(m_a[0])})"
        b_shape = f"({len(m_b)},{len(m_b[0])})"
        raise ValueError(
                        f"shapes {a_shape} and {b_shape} not aligned:"
                        f"{len(m_a[0])} (dim 1) != {len(m_b)} (dim 0)"
                        )

    try:
        # Numpy conversion
        m_a = np.array(m_a)
        m_b = np.array(m_b)

        # Elements verification
        if not np.issubdtype(m_a.dtype, np.number):
            raise TypeError("invalid data type for einsum")
        if not np.issubdtype(m_b.dtype, np.number):
            raise TypeError("invalid data type for einsum")

        result = m_a @ m_b
        return result

    except ValueError as e:
        msg = str(e).splitlines()[0]
        if "setting an array element with a sequence" in msg:
            print("setting an array element with a sequence.")
            sys.exit(0)
        elif "shapes" in msg:
            raise ValueError("shapes not aligned")
        elif "matmul: Input operand 1 has a mismatch" in msg:
            # Incompatible dimensions
            a_shape = f"({len(m_a)},{len(m_a[0])})" if m_a else "(0,0)"
            b_shape = f"({len(m_b)},{len(m_b[0])})" if m_b else "(0,0)"
            raise ValueError(
                            f"shapes {a_shape} and {b_shape} not aligned: "
                            f"{len(m_a[0])} (dim 1) != {len(m_b)} (dim 0)"
                            )
        else:
            raise ValueError(msg)
    except TypeError as e:
        if "scalar" in str(e):
            raise TypeError("Scalar operands are not allowed, use '*' instead")
        raise TypeError("invalid data type for einsum")
