# *******************
# CONSONANTES COMUNES
# *******************


def run(text1: str, text2: str) -> str:
    text1 = text1.lower()
    text2 = text2.lower()
    cconst = ''.join(
        sorted(
            {
                letter1
                for letter1 in text1
                for letter2 in text2
                if (letter1 in text2 and letter2 in text1)
                and (letter1 != ' ' and letter1 not in 'aeiou')
            }
        )
    )

    return cconst


if __name__ == '__main__':
    run('Flat is bEtter than nested', 'Readability counts')
