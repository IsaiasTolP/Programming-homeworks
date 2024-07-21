# *****************
# NÚMEROS PERFECTOS
# *****************


def is_perfect(n: int) -> bool:
    def calc_div() -> list:
        divisors_range_limit = n // 2 + 1
        return [
            possible_div for possible_div in range(2, divisors_range_limit) if n % possible_div == 0
        ]

    if sum(calc_div()) + 1 == n:
        return True
    else:
        return False
