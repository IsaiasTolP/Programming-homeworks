# *************************
# NO ME INTERESAN LOS PARES
# *************************


def run(items: list) -> list:
    current_index = 0
    filter = []

    for item in items:
        if current_index % 2 == 0:
            filter.append(item)
        current_index += 1

    return filter


if __name__ == '__main__':
    run([1, 2, 1, 2, 1, 2])
