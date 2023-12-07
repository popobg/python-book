#! /usr/bin/env python3

import math

class Frac:

    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den
        self.simplify_fract()

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def set_num(self, n):
        self.num = n

    def set_den(self, d):
        self.den = d

    def simplify_fract(self) -> tuple:
        """divide by the greatest common divisor"""
        pgcd = math.gcd(self.num, self.den)
        self.num = self.num // pgcd
        self.den = self.den // pgcd

    def __add__(self, frac) -> tuple:
        return Frac(
            (self.get_num() * frac.get_den()) + (frac.get_num() * self.get_den()),
            (self.get_den() * frac.get_den())
        )

    def __sub__(self, frac) -> tuple:
        return Frac(
            (self.get_num() * frac.get_den()) - (frac.get_num() * self.get_den()),
            (self.get_den() * frac.get_den())
        )

    def __mul__(self, frac):
        return Frac(
            (self.get_num() * frac.get_num()),
            (self.get_den() * frac.get_den())
        )

    def __truediv__(self, frac):
        return Frac(
            (self.get_num() * frac.get_den()),
            (self.get_den() * frac.get_num())
        )

    def __neg__(self):
        return Frac(
            - self.get_num(),
            self.get_den()
        )

    def reciprocal(self):
        return Frac(
            self.get_den(),
            self.get_num()
        )

    def __str__(self) -> str:
        return f"{self.get_num()}/{self.get_den()}"

f = Frac(14, 16)
f2 = Frac(3, 4)
f3 = Frac(1, 2)
f4 = Frac(1, 4)
f_add = f * f2
f_sub = f3 - f4
print(f_add, f_sub)