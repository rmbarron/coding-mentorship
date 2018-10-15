#!/usr/bin/python3

import unittest
import prime_numbers
from parameterized import parameterized

class TestPrimeNumbers(unittest.TestCase):

  @parameterized.expand([
    ("position_5", 5, 11),
    ("position_25", 25, 97),
    ("position_10,000", 10000, 104729)
  ])
  def test_erastothenes_sieve_at_known(self, name, position, expected):
    got = prime_numbers.erastothenes_sieve(position)
    self.assertEqual(got, expected)

  def test_erastothenes_sieve_raises_ValueError(self):
    with self.assertRaises(ValueError):
      prime_numbers.erastothenes_sieve(-1)

if __name__=='__main__':
  unittest.main()