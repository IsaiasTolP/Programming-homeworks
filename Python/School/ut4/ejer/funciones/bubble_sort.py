# **********************
# ORDENANDO CON BURBUJAS
# **********************


def bubble(items: list) -> list:
    copy_items = items.copy()
    for index in range(len(copy_items) - 1):
        if copy_items[index] > copy_items[index + 1]:
            copy_items[index], copy_items[index + 1] = copy_items[index + 1], copy_items[index]
    if items == copy_items:
        return copy_items

    return bubble(copy_items[:-1]) + copy_items[-1:]
