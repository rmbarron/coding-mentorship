#!/usr/bin/python3

import bubblesort
import unittest
from parameterized import parameterized


class TestBubblesort(unittest.TestCase):

  @parameterized.expand([
    ("descending_5-1", [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ("random_5", [25348, 14833, 22081, 30577, 24683],
     [14833, 22081, 24683, 25348, 30577]),
    ("random_10",
     [8702, 19712, 24432, 23450, 8272, 5640, 4973, 32617, 31576, 32078],
     [4973, 5640, 8272, 8702, 19712, 23450, 24432, 31576, 32078, 32617])
  ])
  def test_bubblesort(self, name, base, expected):
    got = bubblesort.bubblesort(base)
    self.assertEqual(got, expected)

if __name__=='__main__':
  unittest.main()