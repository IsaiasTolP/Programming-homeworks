# **********************
# ETIQUETAS EQUIVALENTES
# **********************


def same_letter(letter1: str, letter2: str) -> bool:
    if letter1.lower() == letter2.lower():
        return True
    else:
        return False


def run(tag1: str, tag2: str) -> bool:
    equals = True
    tag1, tag2 = tag1[1 : tag1.find(' ')], tag2[1 : tag2.find(' ')]

    if len(tag1) == len(tag2):
        for pos in range(len(tag1)):
            letter1, letter2 = tag1[pos], tag2[pos]
            if letter1 != letter2:
                if not same_letter(letter1, letter2):
                    equals = False
    else:
        equals = False

    return equals
