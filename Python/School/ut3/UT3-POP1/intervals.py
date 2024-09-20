# ********************
# INTERVALO DESPLEGADO
# ********************


def run(interval: str) -> list:
    splitted_interval = interval.split(',')
    left_limit = int(splitted_interval[0][1:])
    right_limit = int(splitted_interval[1][0:-1])

    if '(' in splitted_interval[0]:
        left_limit += 1
    if ']' in splitted_interval[1]:
        right_limit += 1

    irange = []
    for number in range(left_limit, right_limit):
        irange.append(number)

    return irange


if __name__ == '__main__':
    run('[3,10]')
