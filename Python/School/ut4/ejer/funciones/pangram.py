# ********
# PANGRAMA
# ********

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def is_pangram(text: str) -> bool:
    text = text.replace(' ', '').lower()
    for letter in ALPHABET:
        if letter == 'ñ':
            continue
        if not text.count(letter):
            return False
    return True
