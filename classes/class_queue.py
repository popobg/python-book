#! /usr/bin/env python3

from dataclasses_client import Client

class Queue:
    """data structure"""
    def __init__(self):
        self.queue = []

    def empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def into(self, client: Client):
        self.queue.append(client)

    def out(self, x = 1):
        for i in range(x):
            self.queue.pop(0)

John = Client("John", "retail", 15, 2)
Marc = Client("Marc", "commercial", 2, 15)
Jose = Client("José", "IT", 6, 4)
Maria = Client("Maria", "help", 16, 8)

q = Queue()
print(q.empty())

q.into(John)
q.into(Marc)
q.into(Jose)
q.into(Maria)

print(q.empty())

for i in q.queue:
    print(i, "; ", end = "")
print()

q.out(3)

for i in q.queue:
    print(i, ";", end = "")
print()