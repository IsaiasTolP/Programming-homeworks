# ********************************
# UNA MÉTRICA PARA CADENA DE TEXTO
# ********************************


def run(text: str) -> int:
    characters_number = len(text)
    vocals_number = (
        text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')
    )
    metric = characters_number * vocals_number

    return metric


if __name__ == '__main__':
    run('ordenador')
