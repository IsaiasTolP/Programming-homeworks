# *********************************
# ENCONTRANDO REPETICIÓN DE VOCALES
# *********************************


def run(text: str) -> int:
    text_length = len(text)
    text_length_without_start_vowels = len(text.lstrip('aeiouAEIOUáéíóúÁÉÍÓÚ'))
    nrep = text_length - text_length_without_start_vowels

    return nrep


if __name__ == '__main__':
    run('aaaantequera')
