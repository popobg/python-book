#! /usr/bin/env python3

"""Jeu dans lequel le joueur doit deviner si le nombre généré aléatoirement par l'ordinateur est premier ou non"""

import random

# FUNCTIONS

def is_prime(n):
    """return a boolean whether the number is prime or not
    return None for negative, null or incorrect input"""
    if n == 2:
        return True
    if n % 2 == 0:
        return False
# On cherche de 2 jusqu'à la racine carrée du nombre + 1.
# Il faut convertir en entier car for itère sur des entiers et non des nombres flottants.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_win_text(is_prime_computer_number, computer_number):
    if is_prime_computer_number:
        print(f"Le nombre {computer_number} est un nombre premier. Vous avez gagné !")
    else:
        print(f"Le nombre {computer_number} n'est pas un nombre premier. Vous avez gagné !")

def print_lose_text(is_prime_computer_number, computer_number):
    if is_prime_computer_number:
        print(f"Le nombre {computer_number} est un nombre premier. Vous avez perdu...")
    else:
        print(f"Le nombre {computer_number} n'est pas un nombre premier. Vous avez perdu...")

def controlled_input(prompt):
    """Loop while the user input is not 'oui' or 'non'
    return the first letter of the input"""
    while True:
        user_input = input(prompt).lower()
        if user_input == "" \
        or len(user_input) > 1 and user_input not in ("oui", "non") \
        or len(user_input) == 1 and user_input not in ("o", "n"):
            print("Terme non reconnu. Recommencez.")
            continue
        return user_input[0]

def play_again():
    continue_choice = controlled_input(prompt2)
    if continue_choice == "o":
        play_time = 1
        return play_time
    if continue_choice == "n":
        play_time = 0
        return play_time

# MAIN

play_time = 1
prompt2 = "Voulez-vous continuer à jouer ? (oui ou non)\n> "

while play_time == 1:
    computer_number = random.randrange(2, 101)
    prompt1 = f"Le nombre {computer_number} est-il un nombre premier ? (oui ou non)\n> "
    is_prime_computer_number = is_prime(computer_number)
    player_choice = controlled_input(prompt1)
    # is_prime return True, so we enter this IF if computer_number is prime.
    if is_prime_computer_number:
        if player_choice == "o":
            print_win_text(is_prime_computer_number, computer_number)
            play_time = play_again()
        else:
            print_lose_text(is_prime_computer_number, computer_number)
            play_time = play_again()
    else:
        if player_choice == "n":
            print_win_text(is_prime_computer_number, computer_number)
            play_time = play_again()
        else:
            print_lose_text(is_prime_computer_number, computer_number)
            play_time = play_again()