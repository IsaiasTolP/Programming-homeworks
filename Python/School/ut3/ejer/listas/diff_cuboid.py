# ********************
# CUBOIDES Y VOLÚMENES
# ********************


def run(cuboid1: list, cuboid2: list) -> float:
    vol_1 = 1
    vol_2 = 1

    for side in cuboid1:
        vol_1 *= side
    for side in cuboid2:
        vol_2 *= side

    vol_diff = abs(vol_1 - vol_2)

    return vol_diff


if __name__ == '__main__':
    run([2, 2, 3], [5, 4, 1])
