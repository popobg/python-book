#! /usr/bin/env python3

import random

choices = {
    "p": "pierre",
    "f": "feuille",
    "c": "ciseaux"
}

# random.choice() only know how to randomize in a sequence.
# However, a dictionary is not a sequence and choices.keys() are not a string.
# So we have to change de keys in a list in which the module can randomize.
computer_choice = random.choice(list(choices.keys()))

def controlled_input():
    """Loop while the user input is invalid, then return the input first letter"""
    while True:
        user_input = input("pierre (p), feuille (f), ciseau (c) ?\n> ").lower()
        if user_input == "" \
        or len(user_input) > 1 and user_input not in choices.values() \
        or len(user_input) == 1 and user_input not in choices.keys():
            print("Terme non reconnu. Recommencez.")
            continue
        return user_input[0]

player_choice = controlled_input()

while player_choice == computer_choice:
    print(f"Egalité ! Vous avez tous les deux joué {choices[computer_choice]}. Recommençons.")
    computer_choice = random.choice(list(choices.keys()))
    player_choice = controlled_input()

if player_choice == "p" and computer_choice == "c" \
or player_choice == "c" and computer_choice == "f" \
or player_choice == "f" and computer_choice == "p":
    print(f"Votre adversaire a joué {choices[computer_choice]}. Vous avez gagné !")
else:
    print(f"Votre adversaire a joué {choices[computer_choice]}. C'est perdu...")