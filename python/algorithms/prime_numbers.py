#!/usr/bin/python3

"""
Problem Statement: Find nth prime number given an index within the first 1000
prime numbers.
"""

import math
import sys

def erastothenes_sieve(position):
  """
  Find prime number at nth position by sieving away multiples of non-primes.
  :param position: int index of prime to find.
  :return: int prime number at nth position.
  :raises: ValueError when position is a negative.
  """
  if position < 1:
    raise ValueError("Please provide a positive position.")
  # initialize with known base
  primes = [2, 3]
  counter = 4
  while len(primes) < position:
    is_prime = True
    break_value = math.ceil(math.sqrt(counter))
    for i in primes:
      if i > break_value:
        break
      if (counter % i == 0):
        is_prime = False
        counter += 1
        break
    if not is_prime:
      continue
    primes.append(counter)
    counter += 1
  return primes[position-1]

def main():
  try:
    print(erastothenes_sieve(int(sys.argv[1])))
  except ValueError as e:
    print(e)
    sys.exit(1)

if __name__=='__main__':
  main()