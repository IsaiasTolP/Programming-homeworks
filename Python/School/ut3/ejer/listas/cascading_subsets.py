# ***********************
# SUBCONJUNTOS EN CASCADA
# ***********************


def run(values: list, size: int) -> list:
    cascading = []
    final_index = size

    for index in range(len(values)):
        subset = values[index:final_index]
        if len(subset) == size:
            cascading.append(subset)
            final_index += 1
        else:
            break

    return cascading


if __name__ == '__main__':
    run([1, 2, 3, 4], 3)
