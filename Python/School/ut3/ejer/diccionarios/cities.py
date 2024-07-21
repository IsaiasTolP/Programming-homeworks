# ********************
# DESCIFRANDO CIUDADES
# ********************


def run(cinfo: str) -> dict:
    information = cinfo.split(';')
    for index, info in enumerate(information):
        information[index] = info.split(':')
        information[index][1] = int(information[index][1])
    cities = dict(information)

    return cities


if __name__ == '__main__':
    run('Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;Mumbai:21_357_000')
