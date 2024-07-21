# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(n):
    fact = 1
    if n >= 0:
        for value in range(1, n + 1):
            fact *= value
        return fact
    else:
        return None
