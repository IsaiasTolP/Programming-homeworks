# *************
# N ELEVADO A N
# *************


def run(values: list, power: int) -> int:
    if power >= len(values):
        result = -1
    else:
        element = values[power]
        result = element**power

    return result


if __name__ == '__main__':
    run([1, 2, 3, 4], 2)
