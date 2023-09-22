#! /usr/bin/env python3

import random

def randomize_var(min, max):
    return random.randrange(min, max)

a = randomize_var(0, 11)
b = randomize_var(0, 11)
c = randomize_var(0, 11)

if a != b != c:
    if a > b:
        if b > c:
            print(f"a = {a} > b = {b} > c = {c}")
        elif c > a:
            print(f"c = {c} > a = {a} > b = {b}")
        else:
            print(f"a = {a} > c = {c} > b = {b}")
    else:
        if c > b:
            print(f"c = {c} > b = {b} > a = {a}")
        elif c < a:
            print(f"b = {b} > a = {a} > c = {c}")
        else:
            print(f"b = {b} > c = {c} > a = {a}")
else:
    if a == b == c :
        print(f"a = b = c = {a}")
    elif a == b:
        if c > a:
            print(f"c = {c} > a = b = {b}")
        else:
            print(f"a = b = {b} > c = {c}")
    elif a == c:
        if b > c:
            print(f"b = {b} > a = c = {c}")
        else:
            print(f"a = c = {c} > b = {b}")
    else:
        if a > c:
            print(f"a = {a} > b = c = {c}")
        else:
            print(f"c = b = {b} > a = {a}")