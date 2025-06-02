#!/usr/bin/python3
'''
This module provides a function that returns a list of integers representing
the Pascal's triangle of n
'''


def pascal_triangle(n):
    '''
    The function that represent the Pascal's triangle
    Args:
        n: The size of the triangle
    '''
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev = triangle[-1]
        new = [1]

        for j in range(len(prev) - 1):
            new.append(prev[j] + prev[j + 1])

        new.append(1)
        triangle.append(new)

    return triangle
