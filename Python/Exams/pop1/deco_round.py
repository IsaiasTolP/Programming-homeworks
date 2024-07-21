# ****************************
# REDONDEANDO CON UN DECORADOR
# ****************************


def cround(round_value: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return round(func(*args, **kwargs), round_value)

        return wrapper

    return decorator


@cround(2)
def avg(values: list) -> float:
    result = sum(values) / len(values)
    return result


if __name__ == '__main__':
    avg([6, 3, 9, 3, 5, 4, 5, 7, 2, 3, 6])
