# *****************************
# SUMA DE LA DIAGONAL PRINCIPAL
# *****************************


def run(matrix: list) -> int:
    sum_diagonal = 0
    position = 0
    for row in matrix:
        sum_diagonal += row[position]
        position += 1
    return sum_diagonal


if __name__ == '__main__':
    run([[4, 6, 1], [2, 9, 3], [1, 7, 7]])
