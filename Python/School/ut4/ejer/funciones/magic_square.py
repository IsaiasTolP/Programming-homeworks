# ***************
# CUADRADO MÁGICO
# ***************


def sum_cols(values: list) -> list:
    results = []
    for row in range(len(values)):
        result = 0
        for col in range(len(values[row])):
            result += values[col][row]
        results.append(result)
    return results


def sum_rows(values: list) -> int | list:
    results = [sum(row) for row in values]
    return results


def sum_diagonal(values: list) -> int:
    result = 0
    for index in range(len(values)):
        result += values[index][index]
    return result


def is_magic_square(values: list) -> bool:
    output = True
    col_res = sum_cols(values)
    row_res = sum_rows(values)
    diagonal_res = sum_diagonal(values)
    if values:
        if col_res == row_res and diagonal_res == col_res[0]:
            output = True
        else:
            output = False
    return output
