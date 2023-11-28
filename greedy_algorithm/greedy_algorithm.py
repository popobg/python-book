#! /usr/bin/env python3

"""A program that calculates the change needed from a certain amount of cents.
We randomized the initial number of cents but it could have been an input instead."""

import random

def convert_cent_to_half_dollar(cent):
    half_dollar = cent // 50
    centhd = cent % 50
    return(half_dollar, centhd)

def convert_cent_to_quarter(centhd):
    quarter = centhd // 25
    centqt = centhd % 25
    return(quarter, centqt)

def convert_cent_to_nickel(centqt):
    nickel = centqt // 5
    centnk = centqt % 5
    return(nickel, centnk)

def make_the_change(change):
    money_type = change[0]
    return money_type

def grammatical_agree(money):
    return "s" if money > 1 else ""

def grammatical_agree_penny(money):
    return "ies" if money > 1 else "y"

cent = random.randrange(100)

change1 = convert_cent_to_half_dollar(cent)
half_dollar = make_the_change(change1)

change2 = convert_cent_to_quarter(change1[1])
quarter = make_the_change(change2)

change3 = convert_cent_to_nickel(change2[1])
nickel = make_the_change(change3)
penny = change3[1]

print (f"A partir de {cent} cents, vous obtiendrez {half_dollar} half dollar{grammatical_agree(half_dollar)}, {quarter} quarter{grammatical_agree(quarter)}, {nickel} nickel{grammatical_agree(nickel)} et {penny} penn{grammatical_agree_penny(penny)}.")