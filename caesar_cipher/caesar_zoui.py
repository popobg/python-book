def encode(letter, key):
    # isalpha() check if letter is a letter.
    if not letter.isalpha():
        return letter
    # ord() is a function that return the Unicode code of
    # a one character string.
    # ref is assigned to the code Unicode of 'a' if the variable letter
    # is lowercase, otherwise it is assigned to the code of 'A'.
    ref = ord('a') if letter.islower() else ord('A')
    # letter is convert into its code Unicode and we subtract ref
    # to obtain a number between 0 and 26
    # (number of letters in the alphabet).
    normalized_letter_code = ord(letter) - ref
    # We add the value of key to our number between 0 and 26
    # and we divise it entirely by 26 and keep the remainder.
    # If the result of (normalized_letter_code + key) is between [0, 25],
    # the remainder is equal to (normalized_letter_code + key) ;
    # if it is outside the interval, then the remainder will be
    # inside [0, 25] (like a loop).
    normalized_encoded = (normalized_letter_code + key) % 26
    # normalized_encoded, that is a number, is convert again in a code
    # Unicode by adding ref (that had been subtract).
    encoded = normalized_encoded + ref
    # the function chr() takes a code Unicode and translates it
    # into a string character.
    return chr(encoded)


def decode(letter, key):
    return encode(letter, -key)


def encode_str(string, key):
    return "".join([encode(letter, key) for letter in string])


def decode_str(string, key):
    return encode_str(string, -key)


key = 3
cipher = encode_str("Salut les prouts ! C'est moi Zouizoui !", key)
print(cipher)
print(decode_str(cipher, key))