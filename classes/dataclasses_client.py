#! /usr/bin/env python3

class Client:
    """data-only class"""
    def __init__(self, n, c, t, s):
        self.name = n
        self.category = c   # retail or commercial
        self.time = t
        self.service = s

    def __str__(self):
        return f"{self.name}, {self.category}, {self.time}, {self.service}"

# class Retail(Client):
#     def __init__(self, c):
#         Client.__init__(self, "John", c, 2, 3)

# class Commercial(Client):
#     def __init__(self, c):
#         Client.__init__(self, "Marc", c, 10, 8)
