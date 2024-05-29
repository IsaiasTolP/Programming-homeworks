# *********************
# ENCUENTRA LA INTEGRAL
# *********************


def run(symbol: str) -> str:
    first_number = int(symbol[: symbol.index(',')])
    exponent = int(symbol[symbol.index(',') + 1 :])
    integrated_exponent = exponent + 1
    base = first_number // integrated_exponent
    integral = f'{base}x^{integrated_exponent}'

    return integral


if __name__ == '__main__':
    run('3,2')
