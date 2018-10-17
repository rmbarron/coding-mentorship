#!/usr/bin/python3

"""
Abbreviate a given word into a numeronym. A common example is
"internationalization" becoming "i18n".
"""

from sys import argv

def numeronym(base):
  """
  Reduce a given base word into a numeronym abbreviation.
  :param base: string Word to abbreviate.
  :return: string Abbreviation.
  """
  if len(base) <= 2:
    return base
  return "".join([base[0], str(len(base)-2), base[-1]])

def main():
  if len(argv) != 2:
    print("Please supply only the word to be abbreviated.")
  print(numeronym(argv[1]))

if __name__=='__main__':
  main()