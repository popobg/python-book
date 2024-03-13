import json

def parse(string):
    return string.strip().split(",")

with open("latin.txt", "r")as original_file:
    latin_english = open("latin-english.json", "w")
    english_latin = open("english-latin.json", "w")

    for line in original_file:
        parsed_line = 

    latin_english.close()
    english_latin.close()