""" Write a method that checks if a number is prime or not.

For example:
2 is prime.
4 is not prime.
"""

def is_prime(n):
    "Check if a number is prime."
    return all([n % e != 0 for e in xrange(2,n)]) # All not evenly divisble = a prime