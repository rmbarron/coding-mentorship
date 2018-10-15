#!/usr/bin/python3

"""
Problem Statement: Find nth prime number given an index within the first 1000
prime numbers.
"""

from sys import argv

def erastothenes_sieve(position):
  """
  Find prime number at nth position by sieving away multiples of non-primes.
  :param position: int index of prime to find
  :return: int prime number at nth position
  """
  # initialize with known base
  primes = [2, 3]
  counter = 4
  while len(primes) < position:
    is_prime = True
    for i in primes:
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
  print(erastothenes_sieve(int(argv[1])))

if __name__=='__main__':
  main()