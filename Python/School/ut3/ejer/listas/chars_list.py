# **********************
# DESPLEGANDO CARACTERES
# **********************


def run(texts: list) -> list:
    joined_text = ''.join(texts)
    chars = list(joined_text)

    return chars


if __name__ == '__main__':
    run(['uno', 'dos', 'tres'])
