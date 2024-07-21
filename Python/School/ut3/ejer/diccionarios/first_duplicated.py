# *************************
# PRIMER ELEMENTO DUPLICADO
# *************************


def run(numbers: list) -> int:
    fdup = -1
    values = {}
    for number in numbers:
        if number not in values:
            values[number] = 1
        else:
            values[number] += 1
            fdup = number
            break

    return fdup


if __name__ == '__main__':
    run([2, 3, 5, 3, 2])
