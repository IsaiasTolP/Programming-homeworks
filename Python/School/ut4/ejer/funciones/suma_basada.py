def base_change(num, from_base):
    number_changed = 0
    for pos, digit in enumerate(reversed(num)):
        number_changed += int(digit) * (from_base**pos)
    return number_changed


def add(a, b, from_base=10):
    if from_base != 10:
        a, b = str(a), str(b)
        formatted_a = base_change(a, from_base)
        formatted_b = base_change(b, from_base)
        result = formatted_a + formatted_b
    else:
        result = a + b
    return result


if __name__ == "__main__":
    print(add(11, 10, 8))
    print(add(11, 10, 7))
    print(add(11, 10, 2))
    print(add(11, 10, 1))
