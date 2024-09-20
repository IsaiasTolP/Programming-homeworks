# ********************
# CLAVES DESDE VALORES
# ********************


def run(items: dict, target_value: int) -> tuple:
    source_keys = []
    for item_key, item_val in items.items():
        if item_val == target_value:
            source_keys.append(item_key)
    source_keys = tuple(source_keys)

    return source_keys


if __name__ == '__main__':
    run({'A': 1, 'B': 2, 'C': 3, 'D': 3, 'E': 4}, 3)
