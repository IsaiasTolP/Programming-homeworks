# ***************
# CONTANDO LETRAS
# ***************


def run(sentence: str) -> dict:
    counter = dict.fromkeys(sentence, 0)
    for letter in sentence:
        counter[letter] += 1

    return counter


if __name__ == '__main__':
    run('boom')
