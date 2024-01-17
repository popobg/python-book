#! /usr/bin/env python3

import math

class GCD:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def get_a(self) -> int:
        return self.a

    def get_b(self) -> int:
        return self.b

    def set_a(self, a2: int):
        self.a = a2

    def set_b(self, b2: int):
        self.b = b2

    # this decorator means that the method creates the instance so you can call it while creating the instance
    @classmethod
    # gcd is the name of the instance of GCD
    def sort_arg(gcd, a: int, b: int) -> tuple[int]:
        """sort the arguments given to the instance so that a is the greatest"""
        if a < b:
            return gcd(
                a = b,
                b = a)
        return gcd(
            a = a,
            b = b
        )

    def get_gcd(self) -> int:
        """find the largest positive integer that can divide the two numbers"""
        new_a = self.a
        new_b = self.b
        while new_b > 0:
            remain = new_a % new_b
            new_a = new_b
            new_b = remain
        return new_a

g = GCD.sort_arg(1200, 512)
print(g.get_gcd())

print(math.gcd(1200, 512))