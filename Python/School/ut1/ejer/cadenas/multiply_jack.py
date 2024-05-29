# *************************
# LA MULTIPLICACIÓN DE JACK
# *************************


def run(n: int) -> int:
    digits_number = len(str(abs(n)))
    result = n * 5**digits_number

    return result


if __name__ == '__main__':
    run(3)
