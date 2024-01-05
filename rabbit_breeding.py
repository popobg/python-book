#! /usr/bin/env python3

import random

# female rabbit (doe) breed for the first time at 100 days old.
# Gestation period : 28-32 days, then breed again after 7 days.
# A litter = 3-8 rabbits, 1/2 are does.
# how many rabbits in on year, starting with 3 does and 1 rabbit (4 specimens) ?

# CLASSES

class Rabbit:
    def __init__(self, days: int, gender: bool):
        self.days = days
        self.gender = gender

    def get_days(self):
        return self.days

    def get_gender(self):
        return self.gender

    def set_days(self, add):
        self.days += add

# FUNCTIONS

def reset():
    return []

def breeding(population, days):
    new_population = reset()
    for rabbit in population:
        new_population.append(rabbit)
        if rabbit.get_gender():
            if rabbit.get_days() >= 100:
                for i in range(random.randrange(3, 8)):
                    r = Rabbit(0, True) if i % 2 == 0 else Rabbit(0, False)
                    new_population.append(r)
        rabbit.set_days(random.randrange(35, 39))
    days+= 37
    return new_population, days

# GLOBAL VARIABLES

population = reset()
days = 0

# Start

for i in range(3):
    r = Rabbit(100, True)
    population.append(r)

r = Rabbit(100, False)

while days <= 365:
    population, days = breeding(population, days)

print(len(population))
print(population[0].get_days(), population[-2].get_days())