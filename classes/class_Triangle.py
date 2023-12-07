#! /usr/bin/env python3

import math

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        if not isinstance(x, int) or x not in range(0, 20):
            return
        self._x = x

    def set_y(self, y):
        if not isinstance(y, int) or y not in range(0, 6):
                return
        self._y = y

    def distance(self, p):
        d = (self._x - p.get_x())**2 + (self._y - p.get_y())**2
        return math.sqrt(d)

    def draw(self):
        print(f"({self._x}, {self._y})")

    def move(self, dx, dy):
        self._x = self._x + dx
        self._y = self._y + dy

point1 = Point(2, 4)
point2 = Point(5, 2)
point3 = Point(4, 3)

class Triangle:
    def __init__(self, p0, p1, p2):
        self._v0 = p0
        self._v1 = p1
        self._v2 = p2

    def set_vertices(self, p0, p1, p2):
        self._v0 = p0
        self._v1 = p1
        self._v2 = p2

    def get_vertices(self):
        return (self._v0, self._v1, self._v2)

    def get_center(self):
        return ((self._v0.get_x() + self._v1.get_x() + self._v2.get_x())/3), ((self._v0.get_y() + self._v1.get_y() + self._v2.get_y())/3)

    def move(self, dx, dy):
        self._v0.move(dx, dy)
        self._v1.move(dx, dy)
        self._v2.move(dx, dy)

triangle = Triangle(point1, point2, point3)

triangle.move(2, 3)
print(triangle.get_center())