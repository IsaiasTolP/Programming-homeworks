# ********************************
# ENUMERANDO ELEMENTOS MODO HUMANO
# ********************************


def run(items: str) -> str:
    separated_items = items.split(':')
    separated_items[-2:] = [' and '.join(separated_items[-2:])]

    enum_items = ', '.join(separated_items)

    return enum_items


if __name__ == '__main__':
    run('apples')
