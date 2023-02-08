""" Start counting numbers. 
For multiples of 3, replace the number with "Fizz". 
For the multiples of 5, replace the number with "Buzz". 
For multiples of both 3 and 5, replace them with "FizzBuzz". 
Other just keep the number.
"""

def fizz_buzz(n: int) -> str:
	message = ""

	if n % 3 == 0:  message += "Fizz"
	if n % 5 == 0:  message += "Buzz"
	if not message: message  = str(n)

	return message

if __name__ == '__main__':
	end = 16
	for n in range(1, end+1):
		print(fizz_buzz(n))