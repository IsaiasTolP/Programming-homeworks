# *************************
# DÍGITO DE CONTROL DEL NIF
# *************************


def run(nif: str) -> str:
    all_nif_letter = 'TRWAGMYFPDXBNJZSQVHLCKE'
    nif_letter_index = int(nif) % 23
    nif_letter_selection = all_nif_letter[nif_letter_index]
    wnif = f'{nif}{nif_letter_selection}'

    return wnif


if __name__ == '__main__':
    run('78654355')
