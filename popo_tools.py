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



def parse_csv(file, separator = ",", index = None):
    """parse a csv file into a list of dictionnaries"""
    f = open(file, "r", encoding = "utf-8")

    header_line = f.readline()
    if separator not in header_line:
        raise Exception(f"Separator '{separator}' not found in first line")
    header = [e.strip() for e in header_line.split(separator)]

    parsed = []
    for line in f:
        dic_csv = {}
        list_line = line.split(separator)
        for i, value in enumerate(list_line):
            value = value.strip()
            try:
                value = int(value)
            except:
                try:
                    value = float(value)
                except:
                    pass
            dic_csv[header[i]] = value
        parsed.append(dic_csv)

    if index != None:
        indexed_dic = {}

        if isinstance(index, int):
            index = header[index]

        for dic in parsed:
            index_value = dic[index]
            indexed_dic[index_value] = dic
        parsed = indexed_dic

    f.close()
    return parsed

# le bloc d'instruction ne s'exécute que si on exécute le script dans le terminal
# print(isinstance(a, int))
if __name__ == "__main__":
    planet_dict = parse_csv("planets.csv", index = "Name")
    print(planet_dict)