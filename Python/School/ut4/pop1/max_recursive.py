# *************************************
# CALCULANDO EL MÁXIMO CON RECURSIVIDAD
# *************************************


def rmax(items: list) -> int:
    copy_items = items.copy()
    if len(copy_items) > 1:
        if copy_items[0] <= copy_items[-1]:
            copy_items[0] = copy_items[-1]
        return rmax(copy_items[:-1])
    elif len(copy_items) == 1:
        return copy_items[0]
    else:
        return 0
