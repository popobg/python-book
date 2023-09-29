#! /usr/bin/env python3

"""The purpose of this code is to decypher an encode message \
or to encode a message.
A letter matchs the letter + 6 of the alphabet."""

# VARIABLES

alphabet_lower = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

alphabet_upper = [letter.upper() for letter in alphabet_lower]

str1 = "OkRa Is the closest thing to nylon i'Ve ever eaten."
str2 = "pull the string, and it will follow wherever you wish."
str3 = "let out a little more string on your kite."
str4 = "every string is a different color, a different voice."

str5 = "varr znk yzxotm, gtj oz corr lurruc cnkxkbkx eua coyn."
str6 = "Ans: uqxg oy znk iruykyz znotm zu terut o'bk kbkx kgzkt."

# FUNCTIONS

def encode(letter, key):
    if letter.isupper():
        alphabet = alphabet_upper
    else:
        alphabet = alphabet_lower
    if letter not in alphabet:
        return letter

    letter_index = alphabet.index(letter)
    # If letter_index >= 26 or < 0, modulo 26 make one complete loop of the
    # alphabet and the remainder is the index.
    # If letter_index in [0, 25], it is < 26 so it can not be entirely
    # divided by it, then the remainder is == letter_index.
    final_index = (letter_index + key) % 26
    return alphabet[final_index]

def decode(letter, key):
    return encode(letter, key * -1)

def encode_str(string, key):
    return "".join([encode(i, key) for i in string])

def decode_str(string, key):
    return encode_str(string, key * -1)

# MAIN

print(encode_str(str1, 6))

print(decode_str(str5, 6))

a = encode_str(str1, 6)
print(decode_str(a, 6))