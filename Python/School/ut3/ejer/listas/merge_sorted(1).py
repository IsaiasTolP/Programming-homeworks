# ***************
# MEZCLA ORDENADA
# ***************


def run(values1: list, values2: list) -> list:
    all_values = values1 + values2
    merged = [num for num in all_values]

    for value in merged:
        if merged.count(value) > 1:
            merged.remove(value)

    for index in range(len(merged) - 1):
        min_index = index
        for index_2 in range(index + 1, len(merged)):
            if merged[min_index] > merged[index_2]:
                min_index = index_2
        temp_value = merged[index]
        merged[index] = merged[min_index]
        merged[min_index] = temp_value

    return merged


if __name__ == '__main__':
    run([1, 2, 3, 4], [1, 1, 2, 3, 4, 5])
