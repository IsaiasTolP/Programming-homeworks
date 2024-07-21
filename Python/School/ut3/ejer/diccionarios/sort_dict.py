# *********************
# ORDENE MI DICCIONARIO
# *********************


def run(unsorted_items: dict) -> list:
    sorted_items = []

    for item_key, item_val in unsorted_items.items():
        item_parts = [item_val, item_key]
        sorted_items.append(item_parts)

    sorted_items.sort()
    sorted_items_copy = sorted_items.copy()

    for index, item in enumerate(sorted_items_copy):
        item.reverse()
        sorted_items[index] = tuple(item)

    return sorted_items


if __name__ == '__main__':
    run({'a': 'two', 'b': 'one', 'c': 'three'})
