def input_int(prompt, range=None, quiet=False):
    """show the prompt to the user
    return the number if it is actually an integer
    repeat the question while the number is not an integer"""
    # Check if the original prompt has a space as the last character.
    # If not, add a line break and >space at the end of the prompt.
    if prompt[-1] != " ":
        prompt += "\n> "
    # "while True" = boucle infinie, pour en sortir il faut un return.
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            if not quiet:
                print("La réponse attendue est un nombre entier.")
            continue

        if not range:
                return user_input

        min = range[0]
        max = range[1]
        if user_input < min or user_input > max:
            print(f"Le nombre doit être compris entre {min} et {max}.")
        else:
            return user_input

def input_float(prompt, range=None, quiet=False):
    """show the prompt to the user
    return the number if it is actually a floatting number
    repeat the question while the number is not an floatting number"""
    # On vérifie si le prompt original présente un espace comme dernier caractère.
    # Si ce n'est pas le cas, on ajoute à la fin du prompt un saut de ligne et >\
    # suivi d'un espace.
    if prompt[-1] != " ":
        prompt += "\n> "
    # "while True" = boucle infinie, pour en sortir il faut un return.
    while True:
        try:
            user_input = float(input(prompt))
        except ValueError:
            if not quiet:
                print("La réponse attendue est un nombre entier.")
            continue

        if not range:
                return user_input

        min = range[0]
        max = range[1]
        if user_input < min or user_input > max:
            print(f"Le nombre doit être compris entre {min} et {max}.")
        else:
            return user_input

def search_keywords(string, keywords):
    """search keywords in a string
    return True if at least one keyword is in the string
    return False if it is none in the string"""
    for keyword in keywords:
        if keyword in string:
            return True
    return False

# le bloc d'instruction ne s'exécute que si on exécute le script dans le terminal
if __name__ == "__main__":
    a = input_int("Entrez un nombre entier.", [1, 5])
    print(f"vous avez entré {a} !")
    print(isinstance(a, int))