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

  @parameterized.expand([
    ("fail_case", "fail", "fail"),
    ("success_case", "success", "s5s")
  ])
  def test_unique_numeronym(self, name, base, expected):
    got = numeronym.unique_numeronym(base, "fake_dictionary.txt")
    self.assertEqual(expected, got)

  def test_parse_options(self):
    args = numeronym.parse_options(["--word=localization", "--check_unique"])
    expected = {"check_unique": True, "word": "localization",
                "dictionary_file": "/usr/share/dict/words"}
    self.assertEqual(vars(args), expected)

if __name__=="__main__":
  unittest.main()