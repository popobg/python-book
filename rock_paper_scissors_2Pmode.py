#! /usr/bin/env python3

import os
import time

def clean():
    if os.name == "nt":
        # _ = signifie que la fonction retourne quelque chose mais on l'ignore.
        _ = os.system("cls")
    else:
        _ = os.system("clear")

p = "PIERRE"
f = "FEUILLE"
c = "CISEAUX"
choices = [p, f, c]

player1 = input("Quel est le nom du joueur 1 ?\n> ")
player2 = input("Quel est le nom du joueur 2 ?\n> ")

prompt1 = f"{player1} : pierre (p), feuille (f), ciseaux (c) ?\n> "
prompt2 = f"{player2} : pierre (p), feuille (f), ciseaux (c) ?\n> "


def controlled_input(prompt):
    while True:
        user_input = input(prompt).upper()
        if len(user_input) > 1 and user_input not in choices\
        or len(user_input) == 1 and user_input not in ["P", "C", "F"]:
            print("Terme non reconnu. Recommencez.")
            continue
        if len(user_input) == 1:
            if user_input == "P":
                return p
            if user_input == "F":
                return f
            if user_input == "C":
                return c
        return user_input

# time.sleep() indique le temps en seconde\
# qu'attend le programme avant d'enchaîner avec les commandes suivantes.
# os.system permet d'appeler certaines commandes intervenant sur l'OS\
# (ici le terminal). 'clear' est une commande propre au terminal Linux ;\
# 'cls' pour Windows.
player1_choice = controlled_input(prompt1)
time.sleep(1)
clean()
player2_choice = controlled_input(prompt2)

while player1_choice == player2_choice:
    print("Egalité ! Recommençons.")
    player1_choice = controlled_input(prompt1)
    time.sleep(1)
    clean()
    player2_choice = controlled_input(prompt2)

if player1_choice == p and player2_choice == c\
or player1_choice == c and player2_choice == f\
or player1_choice == f and player2_choice == p:
    print(f"{player1} a gagné ! Bravo {player1}, vous êtes le plus malin.")
else:
    print(f"{player2} a gagné ! {player2}, vous êtes le plus avisé !")