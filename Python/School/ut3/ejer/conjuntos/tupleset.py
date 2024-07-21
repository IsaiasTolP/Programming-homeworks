# ******************
# TUPLAS Y CONJUNTOS
# ******************


def run(input: tuple) -> tuple:
    output = (
        set([duple[0] for duple in input]),
        set([duple[1] for duple in input]),
    )

    return output


if __name__ == '__main__':
    run(((4, 3), (8, 2), (7, 5), (8, 2), (9, 1)))
