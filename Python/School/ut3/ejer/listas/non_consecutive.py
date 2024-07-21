# *******************
# NO ERES CONSECUTIVO
# *******************


def run(values: list) -> int:
    target = None

    if values != []:
        consecutive_num = values[0]
        for value in values:
            if value == consecutive_num:
                consecutive_num += 1
            else:
                target = value
                break

    return target


if __name__ == '__main__':
    run([1, 2, 3, 4, 6, 7, 8])
