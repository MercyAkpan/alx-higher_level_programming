#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = number % 10
if number < 0:
	ldigit = -(ldigit)
print("Last digit of {} is.format(number)")
if (ldigit > 5):
	print(f"{ldigit} and is greater than 5")
elif ldigit == 0:
	print(f"{ldigit} and is 0")
#elif ldigit < 6 and ldigit > 0
#	print(f"{ldigit} and is less than 6 and not 0")
