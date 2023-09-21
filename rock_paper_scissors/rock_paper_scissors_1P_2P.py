#! /usr/bin/env python3

import random
import os
import time

choices = {
    "p": "pierre",
    "f": "feuille",
    "c": "ciseaux"
}

# We defin our functions.

def clean():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def print_win_text_1P(computer_choice):
    print(f"Votre adversaire a joué {choices[computer_choice]}. Vous avez gagné !")

def print_win_text_2P(player1, player2):
    print(f"{player1} a joué {choices[player1_choice]} et {player2} a joué {choices[player2_choice]}. {player1} a gagné, c'est le meilleur !")

def print_lose_text_1P(computer_choice):
    print(f"Votre adversaire a joué {choices[computer_choice]}. C'est perdu...")

def player_number_controlled_input():
    """Loop while the user input is not 'oui' or 'non'"""
    user_input = input ("Ce jeu se joue à un ou deux joueurs. Êtes-vous deux joueurs ? (oui ou non)\n> ")
    while True:
        if user_input == "" \
        or len(user_input) > 1 and user_input not in ("oui", "non") \
        or len(user_input) == 1 and user_input not in ("o", "n"):
            user_input = input("Terme non reconnu. Répondez par oui ou par non : êtes-vous deux joueurs ?\n> ")
            continue
        return user_input[0]

def controlled_input(prompt):
    """Loop while the user input is invalid, then return the input first letter"""
    while True:
        user_input = input(prompt).lower()
        if user_input == "" \
        or len(user_input) > 1 and user_input not in choices.values() \
        or len(user_input) == 1 and user_input not in choices.keys():
            print("Terme non reconnu. Recommencez.")
            continue
        return user_input[0]

def who_wins(computer_choice, player_choice):
    """Return 0 if equality, 1 if computer wins, -1 if player wins"""
    if computer_choice == player_choice:
        return 0
    if computer_choice == "p" and player_choice == "c" \
    or computer_choice == "c" and player_choice == "f" \
    or computer_choice == "f" and player_choice == "p":
        return 1
    else:
        return -1

def play_turn_1P():
    computer_choice = random.choice(list(choices.keys()))
    player_choice = controlled_input(prompt)
    return computer_choice, player_choice

def play_turn_2P():
    player1_choice = controlled_input(prompt1)
    time.sleep(1)
    clean()
    player2_choice = controlled_input(prompt2)
    return player1_choice, player2_choice

# Our functions are defined. We can now call it in our gaming code.

mode_2P = player_number_controlled_input()

if mode_2P == "o":
    player1 = input("Quel est le nom du joueur 1 ?\n> ")
    player2 = input("Quel est le nom du joueur 2 ?\n> ")

    prompt1 = f"{player1} : pierre (p), feuille (f), ciseau (c) ?\n> "
    prompt2 = f"{player2} : pierre (p), feuille (f), ciseau (c) ?\n> "

    player1_choice, player2_choice = play_turn_2P()

    winner = who_wins(player1_choice, player2_choice)

    while winner == 0:
        print(f"Egalité ! Vous avec tous les deux joué {choices[player1_choice]}. Recommençons.")
        player1_choice, player2_choice = play_turn_2P()
        winner = who_wins(player1_choice, player2_choice)

    if winner == 1:
        print_win_text_2P(player1, player2)
    elif winner == -1 :
        print_win_text_2P(player2, player1)

if mode_2P == "n":
    prompt = "pierre (p), feuille (f), ciseau (c) ?\n> "

    computer_choice, player_choice = play_turn_1P()

    winner = who_wins(computer_choice, player_choice)

    while winner == 0:
        print(f"Egalité ! Vous avez tous les deux joué {choices[computer_choice]}. Recommençons.")
        computer_choice, player_choice = play_turn_1P()
        winner = who_wins(computer_choice, player_choice)

    if winner == 1:
        print_lose_text_1P(computer_choice)
    elif winner == -1:
        print_win_text_1P(computer_choice)