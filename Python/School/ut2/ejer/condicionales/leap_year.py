# **************
# AÑOS BISIESTOS
# **************


def run(year: int) -> bool:
    first_condition = year % 4 == 0 and year % 100 != 0
    second_condition = year % 400 == 0

    if first_condition or second_condition:
        is_leap_year = True
    else:
        is_leap_year = False

    return is_leap_year


if __name__ == '__main__':
    run(1900)
