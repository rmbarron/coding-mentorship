#!/usr/bin/python3

import numeronym
import unittest
from parameterized import parameterized

class TestNumeronym(unittest.TestCase):

  @parameterized.expand([
    ("word_internationalization", "internationalization", "i18n"),
    ("word_localization", "localization", "l10n"),
    ("len_2", "at", "at")
  ])
  def test_numeronym(self, name, base, expected):
    got = numeronym.numeronym(base)
    self.assertEqual(got, expected)

if __name__=='__main__':
  unittest.main()