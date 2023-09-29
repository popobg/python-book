#! /usr/bin/env python3

import time

"""The purpose of this code is to decypher an encode message \
or to encode a message.
A letter matchs the letter + 6 of the alphabet."""

start_time = time.time()

alphabet_encode = {
    "a" : "g",
    "b" : "h",
    "c" : "i",
    "d" : "j",
    "e" : "k",
    "f" : "l",
    "g" : "m",
    "h" : "n",
    "i" : "o",
    "j" : "p",
    "k" : "q",
    "l" : "r",
    "m" : "s",
    "n" : "t",
    "o" : "u",
    "p" : "v",
    "q" : "w",
    "r" : "x",
    "s" : "y",
    "t" : "z",
    "u" : "a",
    "v" : "b",
    "w" : "c",
    "x" : "d",
    "y" : "e",
    "z" : "f",
    " " : " ",
    "," : ",",
    "." : ".",
    "'" : "'",
    "!" : "!",
    "?" : "?",
    ":" : ":"
}

alphabet_decode = {
    "g" : "a",
    "h" : "b",
    "i" : "c",
    "j" : "d",
    "k" : "e",
    "l" : "f",
    "m" : "g",
    "n" : "h",
    "o" : "i",
    "p" : "j",
    "q" : "k",
    "r" : "l",
    "s" : "m",
    "t" : "n",
    "u" : "o",
    "v" : "p",
    "w" : "q",
    "x" : "r",
    "y" : "s",
    "z" : "t",
    "a" : "u",
    "b" : "v",
    "c" : "w",
    "d" : "x",
    "e" : "y",
    "f" : "z",
    " " : " ",
    "," : ",",
    "." : ".",
    "'" : "'",
    "!" : "!",
    "?" : "?",
    ":" : ":"
}

def encode(letter):
    return alphabet_encode[letter]

def decode(letter):
    return alphabet_decode[letter]

str1 = "okra is the closest thing to nylon i've ever eaten."
str2 = "pull the string, and it will follow wherever you wish."
str3 = "let out a little more string on your kite."
str4 = "every string is a different color, a different voice."

str5 = "varr znk yzxotm, gtj oz corr lurruc cnkxkbkx eua coyn."
str6 = "Ans: uqxg oy znk iruykyz znotm zu terut o'bk kbkx kgzkt."


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