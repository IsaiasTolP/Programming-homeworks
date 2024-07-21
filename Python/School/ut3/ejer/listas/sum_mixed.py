# ****************
# SUMA HETEROGÉNEA
# ****************


def run(items: list) -> int:
    items = [int(item) for item in items]
    sum_items = sum(items)

    return sum_items


if __name__ == '__main__':
    run([1, '2', 3, '4', 5])
