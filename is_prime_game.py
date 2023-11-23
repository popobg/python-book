#! /usr/bin/env python3

"""A game in which the player has to guess whether the given random number is prime or not"""

import random

# FUNCTIONS

def is_prime(n):
    """return a boolean whether the number is prime or not"""
    if n == 2:
        return True
    if n % 2 == 0:
        return False
# We are searching from 2 to the number's square root + 1.
# Must be convert into an integer because "range" iterate on integers, not float numbers.
    for i in range(3, int(n ** 0.5) + 1):
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

def play_again(play_time):
    prompt2 = "Voulez-vous continuer à jouer ? (oui ou non)\n> "
    continue_choice = controlled_input(prompt2)
    if continue_choice == "o":
        play_time = True
        return play_time
    if continue_choice == "n":
        play_time = False
        return play_time

# MAIN

play_time = True

while play_time == True:
    computer_number = random.randrange(2, 101)
    prompt1 = f"Le nombre {computer_number} est-il un nombre premier ? (oui ou non)\n> "
    is_prime_computer_number = is_prime(computer_number)
    player_choice = controlled_input(prompt1)
    # is_prime return True, so we enter this IF if computer_number is prime.
    if is_prime_computer_number:
        if player_choice == "o":
            print_win_text(is_prime_computer_number, computer_number)
            play_time = play_again(play_time)
        else:
            print_lose_text(is_prime_computer_number, computer_number)
            play_time = play_again(play_time)
    else:
        if player_choice == "n":
            print_win_text(is_prime_computer_number, computer_number)
            play_time = play_again(play_time)
        else:
            print_lose_text(is_prime_computer_number, computer_number)
            play_time = play_again(play_time)