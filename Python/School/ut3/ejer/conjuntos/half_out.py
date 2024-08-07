# ***********
# MITAD FUERA
# ***********


def run(values: set) -> set:
    half_out_values = set()
    for value in values:
        if (result := value // 2) not in values:
            half_out_values.add(result)

    return half_out_values


if __name__ == '__main__':
    run({50, 100, 4, 6, 12})
