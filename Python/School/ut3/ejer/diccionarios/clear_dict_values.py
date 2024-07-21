# **********************
# BORRANDO VALORES CLAVE
# **********************


def run(items: dict) -> dict:
    copy_items = items.copy()

    for item in copy_items:
        copy_items[item] = []

    citems = copy_items

    return citems


if __name__ == '__main__':
    run({'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]})
