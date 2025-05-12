#!/usr/bin/python3
"""
Module to test 6-max_integer
This module provides a unittest test for 6-max_integer
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 2, 1]), 9)

    def test_max_at_middle(self):
        self.assertEqual(max_integer([1, 10, 2]), 10)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_all_equal(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-10, 0, 10]), 10)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_mixed_ints_floats(self):
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_list_with_zero(self):
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))


if __name__ == "__main__":
    unittest.main()