# ********************
# LA CLAVE ES LA CLAVE
# ********************


def run(items: dict) -> dict:
    fitems = {}
    for item_key, item_val in items.items():
        item_key = item_key.split()
        fitems[''.join(item_key)] = item_val

    return fitems


if __name__ == '__main__':
    run({'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']})
