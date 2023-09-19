#! /usr/bin/env python3

import random

p = "pierre"
f = "feuille"
c = "ciseaux"
choices = [p, f, c]

computer_choice = random.choice(choices)

prompt = "pierre (p), feuille (f), ciseaux (c) ?\n> "


def controlled_input(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input == "" \
        or len(user_input) > 1 and user_input not in choices \
        or len(user_input) == 1 and user_input not in ["p", "c", "f"]:
            print("Terme non reconnu. Recommencez.")
            continue
        if len(user_input) == 1:
            if user_input == "p":
                return p
            if user_input == "f":
                return f
            if user_input == "c":
                return c
        return user_input

player_choice = controlled_input(prompt)

while player_choice == computer_choice:
    print(f"Egalité ! Vous avez joué tous les deux joué {computer_choice}. Recommençons.")
    computer_choice = random.choice(choices)
    player_choice = controlled_input(prompt)

# Attention à ne pas créer de variable trop tôt et qu'elle ne s'actualise pas.

if player_choice == p and computer_choice == c \
or player_choice == c and computer_choice == f \
or player_choice == f and computer_choice == p:
    print(f"Votre adversaire a joué {computer_choice}. Vous avez gagné !")
else:
    print(f"Votre adversaire a joué {computer_choice}. C'est perdu...")