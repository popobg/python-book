#! /usr/bin/env python3

import time

"""The purpose of this code is to decypher an encode message \
or to encode a message.
A letter matchs the letter + 6 of the alphabet."""

start_time = time.time()

# VARIABLES

alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

str1 = "okra is the closest thing to nylon i've ever eaten."
str2 = "pull the string, and it will follow wherever you wish."
str3 = "let out a little more string on your kite."
str4 = "every string is a different color, a different voice."

str5 = "varr znk yzxotm, gtj oz corr lurruc cnkxkbkx eua coyn."
str6 = "Ans: uqxg oy znk iruykyz znotm zu terut o'bk kbkx kgzkt."

# FUNCTIONS

def encode(letter):
    if letter in alphabet:
        letter = alphabet.index(letter)
        if letter in range(0, 20):
            letter = alphabet[letter + 6]
        if letter in range(20, 26):
            letter = alphabet[letter - 20]
        return letter
    else:
        return letter

def decode(letter):
    if letter in alphabet:
        letter = alphabet.index(letter)
        if letter in range(0, 6):
            letter = alphabet[letter + 20]
        if letter in range(6, 26):
            letter = alphabet[letter - 6]
        return letter
    else:
        return letter

# MAIN

for i in str1.lower():
    i = encode(i)
    print(i, end = "")
print()

for i in str5.lower():
    i = decode(i)
    print(i, end = "")
print()

for i in str2.lower():
    i = encode(i)
    i = decode(i)
    print(i, end = "")
print()

end_time = time.time()
print((end_time - start_time) * 1000)