# *********************************
# SEPARANDO MAYÚSCULAS Y MINÚSCULAS
# *********************************


def split_case(words: list) -> tuple[list, list]:
    lower_case = []
    upper_case = []
    for word in words:
        if word == word.lower():
            lower_case.append(word)
        elif word == word.upper():
            upper_case.append(word)
    return lower_case, upper_case
