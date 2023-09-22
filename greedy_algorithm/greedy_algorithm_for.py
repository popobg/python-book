#! /usr/bin/env python3

"""A program that calculates the change needed from a certain amount of cents.
We randomized the initial number of cents but it could have been an input instead."""

import random

def grammatical_agree(money):
    if money > 1:
        return "s"
    else:
        return ""

def grammatical_agree_penny(money):
    if money > 1:
        return "ies"
    else:
        return "y"

cent = random.randrange(100)

money = []
rest_of_cent = [cent]

for i in range(5):
    if i == 0:
        money.append(rest_of_cent[-1] // 50)
        rest_of_cent.append(rest_of_cent[-1] % 50)
        divisor = 25
    elif i == 4:
        penny = rest_of_cent[-1]
    else:
        money.append(rest_of_cent[-1] // divisor)
        rest_of_cent.append(rest_of_cent[-1] % divisor)
        divisor = 5

print (f"A partir de {cent} cents, vous obtiendrez {money[0]} half dollar{grammatical_agree(money[0])}, {money[1]} quarter{grammatical_agree(money[1])}, {money[2]} nickel{grammatical_agree(money[2])} et {penny} penn{grammatical_agree_penny(penny)}.")