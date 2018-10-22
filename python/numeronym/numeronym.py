#!/usr/bin/python3

"""
Abbreviate a given word into a numeronym. A common example is
"internationalization" becoming "i18n".
"""

import argparse
from sys import argv

def parse_options(args):
  """
  Parse command line options.
  :param args: list Usually sys.argv, list of arguments to parse.
  :return: Args that are specified by argparse.
  """
  parser = argparse.ArgumentParser()
  parser.add_argument("-w", "--word", help="Word to transform into numeronym.")
  parser.add_argument("--dictionary_file", type=str,
                      default="/usr/share/dict/words",
                      help="File to use as \\n separated dictionary.")
  parser.add_argument("-c", "--check_unique",
                      help="Bool for whether or not to check dictionary for unique word.",
                      action="store_true")

  return parser.parse_args(args=args)

def numeronym(base):
  """
  Reduce a given base word into a numeronym abbreviation.
  :param base: string Word to abbreviate.
  :return: string Abbreviation.
  """
  if len(base) <= 2:
    return base
  return "".join([base[0], str(len(base)-2), base[-1]])

def unique_numeronym(base, dictionary):
  """
  Reduce a given base word into a numeronym abbreviation.
  :param base: string Word to abbreviate.
  :param dictionary: string Path of dictionary to check for uniqueness.
  :return: string Abbreviation or full word, as appropriate.
  """
  check_base = base[:-1]
  contents = []
  with open(dictionary, "r") as f:
    # We could save a few lines of code here, but it becomes harder to read.
    # if any(line.split("\n")[0].startswith(check_base) for line in f):
    #  return base
    contents.extend([line.split("\n")[0] for line in f])
  for entry in contents:
    if entry.startswith(check_base):
      return base
  return numeronym(base)


def main():
  args = parse_options(argv[1:])
  if args.check_unique:
    print(unique_numeronym(args.word, args.dictionary_file))
  else:
    print(numeronym(args.word))

if __name__=='__main__':
  main()