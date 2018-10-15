#!/usr/bin/python3

import unittest
import fibonacci_sequence
from parameterized import parameterized

class TestFibonacciSequence(unittest.TestCase):

    @parameterized.expand([
        ("position_5", 5, 5),
        ("position_25", 25, 75025)
    ])
    def test_fibonacci_at_known(self, name, position, expected):
        got = fibonacci_sequence.fibonacci(position)
        self.assertEqual(got, expected)

if __name__=='__main__':
    unittest.main()