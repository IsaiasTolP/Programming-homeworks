# **************
# POTENCIAS DE 2
# **************


def run(num_powers: int) -> list:
    powers2 = [2**pow_value for pow_value in range(num_powers + 1)]

    return powers2


if __name__ == '__main__':
    run(0)
