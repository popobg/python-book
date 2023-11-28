#! /usr/bin/env python3

"""A program that calculates the change needed from a certain amount of cents.
We randomized the initial number of cents but it could have been an input instead."""

import random

def grammatical_agree(money):
    return "s" if money > 1 else ""

def grammatical_agree_penny(money):
    return "ies" if money > 1 else "y"

initial_cent = random.randrange(100)

cent = initial_cent
money = []

for i in range(4):
    if i == 0:
        money.append(cent // 50)
        cent = cent % 50
        divisor = 25
    elif i == 3:
        penny = cent
    else:
        money.append(cent // divisor)
        cent = cent % divisor
        divisor = 5

print (f"A partir de {initial_cent} cents, vous obtiendrez {money[0]} half dollar{grammatical_agree(money[0])}, {money[1]} quarter{grammatical_agree(money[1])}, {money[2]} nickel{grammatical_agree(money[2])} et {penny} penn{grammatical_agree_penny(penny)}.")