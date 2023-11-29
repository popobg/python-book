#! /usr/bin/env python3

'''The goal is to code a program working on a Command-Line Interface.
The program convert fahrenheit to celsius and vice versa.'''

import sys

def farhenheit_to_celsius(number):
    return ((number -32) * (5/9))

def celsius_to_farhenheit(number):
    return ((number * (9/5)) + 32)

def prog_usage():
    """print an error message and explanation in case of unrecognized format
    then exit the program"""
    print("usage : conversion_short <expression>\nSaisir une expression comme '70f' pour des Fahrenheit ou '25c' pour des Celsius.")
    exit()

# Check if we have two arg in our CLI :
# the first is the name of the program,
# the second is the number to convert and its unit.
# if not, print the error message
if len(sys.argv) < 2:
    prog_usage()

# taking the number to convert and its unit (second parameter in the CLI)
to_convertstr = sys.argv[1].lower()
# collect the unit, the last character of the CLI
unit = to_convertstr[-1]

# check if we have the right unit (c or f expected).
# if not, print the error message
if unit not in ["f", "c"]:
    prog_usage()

# check if a float number was given.
# if not, print the error message
try:
    to_convert = float(to_convertstr.strip(to_convertstr[-1]))
except ValueError:
    prog_usage()

# make conversion according to the unit given
# print 2 numbers after the decimal mark
if unit == "f":
    print(f"{farhenheit_to_celsius(to_convert):.2f}°C")
else:
    print(f"{celsius_to_farhenheit(to_convert):.2f}°F")