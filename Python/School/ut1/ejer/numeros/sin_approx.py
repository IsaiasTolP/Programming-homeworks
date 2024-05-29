# *******************
# APROXIMANDO EL SENO
# *******************


def run(x: float) -> float:
    x_multi = x * (180 - x)
    num_result = 4 * x_multi
    den_result = 40500 - x_multi
    sin = (num_result) / (den_result)

    return sin


if __name__ == '__main__':
    run(90)
