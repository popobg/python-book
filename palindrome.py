#! /usr/bin/env python3

def is_palindrome(string):
    modified_string = string.lower().strip().replace(" ", "")
    return modified_string == modified_string[::-1]

user_input = input("Type a word or a sentence:\n> ")

if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")