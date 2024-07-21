# *****************************
# SOMOS IGUALES, PERO DISTINTOS
# *****************************


def run(items: list) -> bool:
    all_same = True

    for item in items:
        if items[0] != item:
            all_same = False

    return all_same


if __name__ == '__main__':
    run([1, 1, 1, 1, 1, 1])
