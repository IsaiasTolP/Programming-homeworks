# *******************
# FIBONACCI GENERADOR
# *******************


def fibonacci_gen(to_gen: int):
    value_1, value_2 = 0, 1
    for _ in range(to_gen):
        yield value_1
        value_1, value_2 = value_2, value_2 + value_1


def run(n: int):
    return [value for value in fibonacci_gen(n)]
