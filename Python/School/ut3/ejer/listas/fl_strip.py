# ****************
# TROCEADO EXTREMO
# ****************


def run(numbers: str) -> str:
    numbers = numbers.split(',')
    numbers = numbers[1:-1]
    strip_numbers = ' '.join(numbers)

    return strip_numbers


if __name__ == '__main__':
    run('1,2,3')
