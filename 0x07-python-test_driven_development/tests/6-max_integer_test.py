#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer"""

    def test_DefaultArguments(self):
        """Test with default arguments"""
        self.assertIsNone(max_integer(), None)

    def test_TooManyArguments(self):
        """Test with extra arguments"""
        self.assertRaisesRegex(
            TypeError, " 0 to 1 positional arguments ", max_integer, [], []
        )

    def test_NonIterableArguments(self):
        """Test with non-iterable arguments"""
        self.assertRaises(TypeError, max_integer, 0)
        self.assertRaises(TypeError, max_integer, None)

    def test_BadIterableArguments(self):
        """Test with a iterable non-list arguments"""
        self.assertEqual(max_integer('ABC'), 'C')
        self.assertEqual(max_integer([[], [0], [0, 0]]), [0, 0])
        self.assertRaises(TypeError, max_integer, [0, []])

    def test_GoodIterableArguments(self):
        """Test with a non-iterable argument"""
        self.assertEqual(max_integer([0, float("inf")]), float("inf"))
        self.assertEqual(max_integer([0, float("-inf")]), 0)
        self.assertEqual(max_integer([0, float("nan"), 1]), 1)
        self.assertNotEqual(max_integer([float("nan"), 0, 1]), 1)
