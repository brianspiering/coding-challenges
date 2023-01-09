""" Write a program that prints the numbers from 1 to 100. But for multiples of three print 'Fizz' instead of the number and for the multiples of five print 'Buzz'. For numbers which are multiples of both three and five print 'FizzBuzz'.
"""

def fizzbuzz(n):
    message = ""
    if n % 3 == 0:
        message += "Fizz"
    if n % 5 == 0:
        message += "Buzz"
    if not message:
        message = n
    return message

if __name__ == "__main__":
    limit = 100
    print [fizzbuzz(n) for n in xrange(1,limit+1)]