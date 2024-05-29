# **************************
# BUSCANDO EL SIGLO ADECUADO
# **************************


def run(year: int) -> int:
    century = (year + 99) // 100

    return century


if __name__ == '__main__':
    run(1705)
