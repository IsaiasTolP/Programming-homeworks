# ****************
# EN BINARIO CLARO
# ****************


def run(number: int) -> str:
    num_in_bin = bin(number)
    nbin = num_in_bin[2:]

    return nbin


if __name__ == '__main__':
    run(233)
