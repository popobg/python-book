#! /usr/bin/env python3

# L'objectif est de créer un programme capable de convertir les °F
# en °C et inversement.

import popo_tools

def fahrenheit_to_celsius():
    fahrenheit_data = popo_tools.input_float("Quelle est votre température en degré Fahrenheit (°F) ?")
    celsius_data = (fahrenheit_data - 32) * (5/9)
    return celsius_data

def celsius_to_fahrenheit():
    celsius_data = popo_tools.input_float("Quelle est votre température en degré Celsius (°C) ?")
    fahrenheit_data = (celsius_data * 9/5) + 32
    return fahrenheit_data

conversion_choice = 0
choices = [1, 2]

while conversion_choice not in choices:
    conversion_choice = popo_tools.input_int(f"Vous devez choisir une des options suivantes en répondant par 1 ou par 2 :\nConvertir en degrés Celsius (option 1) ou convertir en degrés Fahrenheit (option 2) ?", quiet=True)

if conversion_choice == 1:
    print(f"L'équivalent en degrés Celsius est {fahrenheit_to_celsius():.2f}.")
elif conversion_choice == 2:
    print(f"L'équivalent en degrés Fahrenheit est {celsius_to_fahrenheit():.2f}.")