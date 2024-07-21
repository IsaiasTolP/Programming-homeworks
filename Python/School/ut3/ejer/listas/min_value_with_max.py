# ************
# VALOR MÁXIMO
# ************


def run(values: list) -> int:
    copy_values = values.copy()

    while len(copy_values) > 1:
        copy_values.remove(max(copy_values))

    min_value = copy_values[0]

    return min_value


if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])
