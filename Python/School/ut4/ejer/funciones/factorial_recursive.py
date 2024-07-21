# *******************************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO (CON RECURSIVIDAD)
# *******************************************************


def factorial(value):
    if value < 0:
        return None
    elif value == 0:
        return 1
    else:
        return value * factorial(value - 1)
