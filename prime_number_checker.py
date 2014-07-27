""" Write a method that checks if a number is prime or not.
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself.

For example:
2 is prime.
4 is not prime.
"""

def is_prime(n):
    "Check if number is prime with list comprhension."
    return not any([n % _ == 0 for _ in xrange(2,n)])