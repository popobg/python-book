#! /usr/bin/env python3

import os, time
import json

def clean():
    if os.name == "nt":
        # _ = signifie que la fonction retourne quelque chose mais on l'ignore.
        _ = os.system("cls")
    else:
        _ = os.system("clear")

with open("would_you_rather.json", "r") as f:
    data = json.load(f)

print('Ce jeu est un "Tu préfères" édition Spéciale Zouizoui.')
time.sleep(1)
print("Le principe est de choisir entre les deux propositions qui te sont faites, celle que tu préfères.")
time.sleep(1)
print("A toi de jouer ! Appuie sur Entrée pour continuer.")
input()

# Laissez la possibilité de passer une fois si choix trop difficile.