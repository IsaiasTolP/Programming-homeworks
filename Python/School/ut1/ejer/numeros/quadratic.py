# *************************
# ECUACIÓN DE SEGUNDO GRADO
# *************************


def run(a: int, b: int, c: int) -> tuple:
    divider = 2 * a
    multiply = 4 * a * c
    potency = b**2
    root_result = (potency - multiply) ** 0.5
    x1 = (-b + root_result) / (divider)
    x2 = (-b - root_result) / (divider)

    return x1, x2


if __name__ == '__main__':
    run(4, -6, 2)
