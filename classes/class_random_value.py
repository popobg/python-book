#! /usr/bin/env python3

import random

class Random_value:
    """give a random value between 0 and 100"""
    def __init__(self):
        self.val = random.randrange(0, 100)

t = ()
for i in range(0, 100):
    v = Random_value()
    t += (v,)

# search for the smallest value and its location in the tuple t
max = (0, 100)
for i, inst in enumerate(t):
    new_max = inst.val
    if new_max < max[1]:
        max = (i, new_max)
print(max)