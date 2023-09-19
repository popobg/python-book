def input_int(prompt, range=None):
    """affiche le prompt à l'utilisateur
    retourne le nombre si c'est effectivement un entier
    répète la question tant que ce nombre n'est pas un entier"""
    # On vérifie si le prompt original présente un espace comme dernier caractère.
    # Si ce n'est pas le cas, on ajoute à la fin du prompt un saut de ligne et >\
    # suivi d'un espace.
    if prompt[-1] != " ":
        prompt += "\n> "
    # "while True" = boucle infinie, pour en sortir il faut un return.
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
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
    """cherche des mots-clés dans une string
    retourne True si au moins un des mots-clés est présent dans la string
    retourne False si aucun n'est présent"""
    for keyword in keywords:
        if keyword in string:
            return True
    return False

# le bloc d'instruction ne s'exécute que si on exécute le script dans le terminal
if __name__ == "__main__":
    a = input_int("Entrez un nombre entier.", [1, 5])
    print(f"vous avez entré {a} !")
    print(isinstance(a, int))