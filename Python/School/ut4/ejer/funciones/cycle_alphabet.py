# *****************
# ALFABETO CIRCULAR
# *****************

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def run(max_letters: int) -> str:
    text = ''
    if max_letters:
        for index, letter in enumerate(ALPHABET, start=1):
            text += letter
            if index == max_letters:
                return text
        if len(text) < max_letters:
            return text + run(max_letters - len(text))

    return text


if __name__ == '__main__':
    run(0)
