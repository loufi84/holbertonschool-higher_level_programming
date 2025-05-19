#!/usr/bin/python3
'''
This module provides an algorithm to solve the N queens puzzle.
It prints all possible solutions for a given N >= 4.
'''
import sys


def safe(queens, row, col):
    '''
Checks whether placing a queen at a given position is safe.

    Args:
        queens (list of int): Current positions of already-placed queens.
                              Index = row, value = column.
        row (int): Current row to check.
        col (int): Column to test for the queen.

    Returns:
        bool: True if the position is safe, False otherwise.
    '''
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(n, row=0, queens=[], solutions=[]):
    '''
    Recursively finds all solutions to the N queens puzzle.

    Args:
        n (int): Size of the chessboard (N*N).
        row (int): Current row to place a queen.
        queens (list of int): Current state of the board (queen positions).
        solutions (list): Accumulator for valid solutions.
    '''
    if row == n:
        solutions.append([[r, c] for r, c in enumerate(queens)])
        return
    for col in range(n):
        if safe(queens, row, col):
            solve(n, row + 1, queens + [col], solutions)


def main():
    '''
    Main function to validate arguments and trigger the N queens solver.

    Validates the user input and prints all solutions.
    '''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve(n, solutions=solutions)
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
