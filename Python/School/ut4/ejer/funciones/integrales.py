def f(x):
    return x**2


def float_range(x_start, x_end, precision):
    distance = abs(x_end - x_start)
    current_pos = 0
    heights = []
    while current_pos < distance:
        current_pos += precision
        heights.append(f(current_pos))
    return heights


def calc_area(precision, heights):
    result = 0
    for index in range(len(heights)):
        result += (rectangle_area := precision * heights[index])
    return result


x_start = 0
x_end = 2
precision = 0.001

heights = float_range(x_start, x_end, precision)
integral_res = calc_area(precision, heights)
print(integral_res)
