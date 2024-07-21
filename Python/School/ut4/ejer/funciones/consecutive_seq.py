# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************

counter = 0


def consecutive_seq(items: list, target_count: int, counter: int = 1) -> int | bool:
    print(counter)
    if counter == target_count:
        return items[0]
    elif target_count == 1:
        return items[0]
    if len(items) >= 2:
        if items[0] == items[1]:
            return consecutive_seq(items[1:], target_count, counter=counter + 1)
        else:
            return consecutive_seq(items[1:], target_count, counter=1)
    else:
        return False
