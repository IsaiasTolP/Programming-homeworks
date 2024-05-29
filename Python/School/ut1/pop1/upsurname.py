# ********************************
# APELLIDO EN MAYÚSCULAS, SUMA UNO
# ********************************


def run(fullname: str) -> int:
    comma_index = fullname.index(',')

    name_first_letter_index = comma_index + 1
    name = fullname[name_first_letter_index:]
    surname = fullname[:comma_index]

    is_capital_letters = surname.isupper()
    name_length = len(name)

    fmetric = name_length + is_capital_letters

    return fmetric


if __name__ == '__main__':
    run('Kernighan,Brian')
