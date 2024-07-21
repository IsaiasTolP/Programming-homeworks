# **********************
# MEZCLANDO DICCIONARIOS
# **********************


def run(d1: dict, d2: dict) -> dict:
    all_dicts = []
    for char1, char2 in d1.items():
        item = char1, char2
        all_dicts.append(item)
    for char1, char2 in d2.items():
        item = char1, char2
        all_dicts.append(item)

    merged = dict(all_dicts)

    return merged


if __name__ == '__main__':
    run({'a': 1, 'b': 2}, {'a': 3, 'c': 4})
