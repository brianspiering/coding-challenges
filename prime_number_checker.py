""" Write a method that checks if a number is prime or not.

For example:
2 is prime.
4 is not prime.
"""

def is_prime(n):
    "Check if a number is prime by checking all values below n are not be modulus zero. Ingoring 1."
    return all([n % e != 0 for e in xrange(2,n)] if n > 1 else [False])