#! /usr/bin/env python3

import random

def randomize_var(min, max):
    return random.randrange(min, max)

a = randomize_var(0, 11)
b = randomize_var(0, 11)
c = randomize_var(0, 11)

sorted_numbers = [a, b, c]
sorted_numbers.sort()

if sorted_numbers[0] != sorted_numbers[1] != sorted_numbers[2]:
    print(f"{sorted_numbers[0]} < {sorted_numbers[1]} < {sorted_numbers[2]}")
elif sorted_numbers[0] == sorted_numbers[1] == sorted_numbers[2]:
    print(f"{a} = {b} = {c}")
else:
    if sorted_numbers[0] == sorted_numbers[1]:
        print(f"{sorted_numbers[0]} = {sorted_numbers[1]} < {sorted_numbers[2]}")
    else:
        print(f"{sorted_numbers[0]} < {sorted_numbers[1]} = {sorted_numbers[2]}")