#! /usr/bin/env python3

import random
import popo_tools

# Return a random number between 0 and 10.
random_number = random.randrange(11)

player_number = popo_tools.input_int("Devinez le nombre choisi entre 0 et 10.", [0, 10])

while player_number != random_number:
    if player_number < random_number:
        print("C'est plus !")
    else:
        print("c'est moins !")
    player_number = popo_tools.input_int("Devinez le nombre choisi entre 0 et 10.")
print("C'est gagné !")