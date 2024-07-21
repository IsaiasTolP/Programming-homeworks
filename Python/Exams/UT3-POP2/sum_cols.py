# ****************
# SUMANDO COLUMNAS
# ****************
from pathlib import Path


def run(data_path: Path) -> tuple:
    f = open(data_path)
    numbers = [line.split() for line in f]
    results_row = numbers[0]

    for row in numbers[1:]:
        for num_index, number in enumerate(row):
            results_row[num_index] = int(number) + int(results_row[num_index])
    f.close()
    csum = tuple(results_row)

    return csum


if __name__ == '__main__':
    run('data/sum_cols/data1.txt')
