# ************************
# DÍGITOS EN ORDEN INVERSO
# ************************


def run(number: int) -> list:
    number = str(number)
    rev_digits = [int(value) for value in number]
    rev_digits.reverse()

    return rev_digits


if __name__ == '__main__':
    run(35231)
