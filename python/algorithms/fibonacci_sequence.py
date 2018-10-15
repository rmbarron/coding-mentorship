#!/usr/bin/python3

"""
Fibonacci sequence is the sum of the two preceding numbers.
Example sequence: 1 1 2 3 5 8 13

Problem Statement: Find the number at nth position of the sequence.
"""

from sys import argv

def fibonacci(position):
    """
    Find the int in the fibonacci sequence at the given position
    :param position: int position of int to return
    :return: int number within fibonacci sequence
    """
    # Initialize with first two knowns
    sequence = [1, 1]
    for i in range(1, position):
        sequence.append(sequence[i]+sequence[i-1])
    return sequence[position-1]

def main():
    if len(argv) == 1:
        print("Please supply the position to find in the sequence.")
        return 1
    print(fibonacci(int(argv[1])))

if __name__=='__main__':
    main()
