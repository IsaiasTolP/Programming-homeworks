# *******************************
# CONTANDO VOCALES (EN RECURSIVO)
# *******************************

VOWELS = 'aeiou'


def count_vowels(text: str) -> int:
    if len(text) == 0:
        return 0
    char = text[0]
    if char in VOWELS:
        return 1 + count_vowels(text[1:])
    return count_vowels(text[1:])
