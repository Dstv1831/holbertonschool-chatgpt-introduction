#!/usr/bin/python3

"""Module providing a function printing python version."""
import sys


def factorial(n):
    """Function that prints the factorial"""
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

f = factorial(int(sys.argv[1]))
print(f)
