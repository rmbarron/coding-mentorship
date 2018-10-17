#!/usr/bin/python3

from sys import argv

def main(args):
  print("I am: {}".format(args[0]))
  print("You gave me: {}".format(args[1:]))

main(argv)
