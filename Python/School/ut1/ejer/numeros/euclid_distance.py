# ******************
# DISTANCIA EUCLÍDEA
# ******************


def run(x1: float, y1: float, x2: float, y2: float) -> float:
    side_1 = (x2 - x1) ** 2
    side_2 = (y2 - y1) ** 2
    distance = (side_1 + side_2) ** 0.5
    return distance


if __name__ == '__main__':
    run(3, 5, -7, -4)
