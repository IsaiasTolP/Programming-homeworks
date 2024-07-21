# *******************************
# DECORANDO CON VALORES ABSOLUTOS
# *******************************


def fabs(func):
    def wrapper(a, b):
        return func(abs(a), abs(b))

    return wrapper


@fabs
def fprod(a, b):
    return a * b
