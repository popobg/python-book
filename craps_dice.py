#! /usr/bin/env python3

"""Also known as the seven-eleven
The shooter rolls two dices."""

# Si on fait 7 ou 11 au premier tour, on gagne.
# Si on fait 2, 3 ou 12 au premier tour, on perd.
# Ensuite on joue jusqu'à soit faire 7 (perdu), soit faire le même nombre de point que le jet précédent (gagné).

import random

def roll_dice():
    # on peut aussi parfaitement faire direct random.randint(1,12)
    return random.randint(2, 12)

def print_win(roll):
    print(f"You score {roll}. Congratulations, you win!")

def print_lose(roll):
    print(f"You score {roll}. Sorry, you lose.")

def print_point(roll):
    print(f"You score {roll}. We continue.")

input("roll dice?")
first_roll = roll_dice()

first_roll_win = [7, 11]
first_roll_lose = [2, 3, 12]

# Comment arrêter le programme si les deux premiers ifs se réalisent ?
if first_roll in first_roll_win:
    print_win(first_roll)
    exit()
elif first_roll in first_roll_lose:
    print_lose(first_roll)
    exit()
else:
    print_point(first_roll)
    point = first_roll

while True:
    input("roll dice?")
    roll = roll_dice()
    if roll == 7:
        print_lose(roll)
        exit()
    elif roll == point:
        print_win(roll)
        exit()
    else:
        print_point(roll)
        point = roll