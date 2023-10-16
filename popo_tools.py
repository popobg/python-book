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
                print("The answer must be an integer.")
            continue

        if not range:
                return user_input

        min = range[0]
        max = range[1]
        if user_input < min or user_input > max:
            print(f"The number must be between {min} and {max}.")
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
                print("The answer must be a number.")
            continue

        if not range:
                return user_input

        min = range[0]
        max = range[1]
        if user_input < min or user_input > max:
            print(f"The number must be between {min} and {max}.")
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

def parse_csv(file, separator = ", "):
    """parse a csv file into a list of dictionnaries"""
    f = open(file, "r", encoding = "utf-8")
    header = f.readline().split(separator)
    parsed = []
    for line in f:
        dic_csv = {}
        list_line = line.split(separator)
        for i in range(len(list_line)):
            dic_csv[header[i].strip()] = list_line[i].strip()
        parsed.append(dic_csv)
    f.close()
    return parsed

# le bloc d'instruction ne s'exécute que si on exécute le script dans le terminal
if __name__ == "__main__":
    a = input_int("Enter an integer.", [1, 5])
    print(f"You choose {a} !")
    print(isinstance(a, int))