# **************
# EL LOBO ACECHA
# **************


def run(farm: list) -> str:
    if farm[-1] == 'lobo':
        msg = 'No te quiero ver más por aquí, lobo'
    else:
        non_programmer_wolf_pos = farm.index('lobo') + 1
        farm_size = len(farm)
        non_programmer_sheep_pos = farm_size - non_programmer_wolf_pos
        msg = f'Cuidado oveja {non_programmer_sheep_pos}, el lobo te va a comer'

    return msg


if __name__ == '__main__':
    run(['oveja', 'oveja', 'lobo', 'oveja'])
