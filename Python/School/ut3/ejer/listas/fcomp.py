# *********************************
# APLICANDO FUNCIÓN POR COMPRENSIÓN
# *********************************


def run(xmin: int, xmax: int) -> list:
    values_stream = ''

    for x in range(xmin, xmax + 1):
        result = 3 * x + 2
        values_stream += f'{result},'

    values_stream = values_stream[:-1]
    values = [int(value) for value in values_stream.split(',')]

    return values


if __name__ == '__main__':
    run(0, 10)
