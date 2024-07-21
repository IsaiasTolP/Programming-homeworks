range_start = -9
range_end = 9

quadratic_function = range_start**2 - 6 * range_start + 3
result = quadratic_function + 1

for x in range(range_start, range_end):
    quadratic_function = x**2 - 6 * x + 3
    if quadratic_function < result:
        min_result = quadratic_function
        x_result = x
    result = quadratic_function

print(f'El valor de x que está buscando es {x_result} y su resultado {min_result}.')
