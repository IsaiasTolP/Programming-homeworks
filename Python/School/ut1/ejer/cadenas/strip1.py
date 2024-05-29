# *************************
# QUITANDO PRIMERO Y ÚLTIMO
# *************************


def run(text: str) -> str:
    last_letter = len(text) - 1
    stext = text[1:last_letter]

    return stext


if __name__ == '__main__':
    run('What can I do')
