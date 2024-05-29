# ********************
# UNA SENCILLA FUNCIÓN
# ********************


def run(a: int, b: int) -> float:
    absolute_a = abs(a)
    absolute_b = abs(b)

    numerator = -a * absolute_b**0.5
    denominator = b * a**2 * absolute_a**0.5
    G_result = numerator / denominator

    G = round(G_result, 7)

    return G


if __name__ == '__main__':
    run(-5, 7)
