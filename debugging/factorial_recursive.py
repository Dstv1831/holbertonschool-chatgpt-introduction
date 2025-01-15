#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
    n (int): The number for which to calculate the factorial. Should be a non-negative integer.

    Returns:
    int: The factorial of the given number. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the first command-line argument, convert it to an integer, and calculate the factorial.
f = factorial(int(sys.argv[1]))
print(f)