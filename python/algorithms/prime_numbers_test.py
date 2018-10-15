#!/usr/bin/python3

import unittest
import prime_numbers
from parameterized import parameterized

class TestPrimeNumbers(unittest.TestCase):

  @parameterized.expand([
    ("position_5", 5, 11),
    ("position_25", 25, 97)
  ])
  def test_erastothenes_sieve_at_known(self, name, position, expected):
    got = prime_numbers.erastothenes_sieve(position)
    self.assertEqual(got, expected)

if __name__=='__main__':
  unittest.main()