#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = -number
else:
    n = number
digit = n % 10
pref = f"Last digit of {number:d} is"
if number < 0:
    digit = -digit
if digit > 5:
    print(f"{pref} {digit:d} and is greater than 5")
elif digit < 6 and digit != 0:
    print(f"{pref} {digit:d} and is less than 6 and not 0")
elif digit == 0:
    print(f"{pref} {digit:d} and is 0")
