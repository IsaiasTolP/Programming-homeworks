# *******************
# SEPARANDO EL TIEMPO
# *******************


def run(seconds: int) -> tuple:
    HOUR_TO_SEC = 3600
    MIN_TO_SEC = 60

    hours = seconds // HOUR_TO_SEC
    minutes = seconds % HOUR_TO_SEC // MIN_TO_SEC
    seconds = seconds % MIN_TO_SEC
    return hours, minutes, seconds


if __name__ == '__main__':
    run(31256)
