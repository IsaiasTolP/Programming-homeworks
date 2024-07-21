# **************
# SUMA RECORTADA
# **************


def run(values: list) -> int:
    copy_values = values.copy()

    if len(copy_values) > 2:
        max_value = max(copy_values)
        min_value = min(copy_values)

        for _ in range(copy_values.count(max_value)):
            copy_values.remove(max_value)
        for _ in range(copy_values.count(min_value)):
            copy_values.remove(min_value)

        tsum = sum(copy_values)
    else:
        tsum = 0

    return tsum


if __name__ == '__main__':
    run([6, 2, 1, 8, 10])
