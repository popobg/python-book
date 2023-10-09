# Word processing systems sometimes need to shorten a word to make it fit
# on a line. Write a function that takes a string containing a single word and
# decides where to hyphenate it. A hyphen can occur before the endings -ing,
# -ed, -ate, -tion, or -ment. It could also occur after a prefix: pre-, post-, para-,
# pro-, con-, or com-. Otherwise, place a hyphen somewhere in the middle of
# the word. The function should return a tuple containing the first and second
# half of the word split at the hyphen.

def search_suffix_start(string):
    suffix = ["ing", "ed", "ate", "tion", "ment"]
    for i in suffix:
        if string.endswith(i):
            return string.rfind(i)
    return -1

def search_prefix_end(string):
    prefix = ["pre", "post", "para", "pro", "con", "com"]
    for i in prefix:
        if string.startswith(i) == i:
            return len(i)
    return -1

def hyphenate(string):
    # if suffix_index != -1 and prefix_index != -1:
    #     prefix1 = string[:prefix_index]
    #     new_stringps = string[prefix_index:suffix_index]
    #     suffix1 = string[suffix_index:]
    #     return(prefix1, new_stringps, suffix1)
    suffix_index = search_suffix_start(string)
    if suffix_index != -1:
        suffix2 = string[suffix_index:]
        new_strings = string[:suffix_index]
        return (new_strings, suffix2)
    prefix_index = search_prefix_end(string)
    if prefix_index != -1:
        prefix2 = string[:prefix_index]
        new_stringp = string[prefix_index:]
        return (prefix2, new_stringp)
    else:
        separator_index = len(string) // 2
        pre_hyphen = string[:separator_index]
        post_hyphen = string[separator_index:]
        return (pre_hyphen, post_hyphen)

print(hyphenate("papagalosng"))
print(hyphenate("prepapagalosin"))
print(hyphenate("papagalosing"))
print(hyphenate("prepapagalosing"))
print(hyphenate("contraste"))
print(hyphenate("syed"))