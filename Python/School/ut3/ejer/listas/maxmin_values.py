# *********************
# VALOR MÁXIMO Y MÍNIMO
# *********************


def run(values: list) -> tuple:
    max_value = values[0]
    for num in values[1:]:
        if num > max_value:
            max_value = num

    min_value = values[0]
    for num in values[1:]:
        if num < min_value:
            min_value = num

    return max_value, min_value


if __name__ == '__main__':
    run([4, 6, 2, 1, 9, 63, -134, 566])
