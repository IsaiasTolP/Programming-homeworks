# *******************
# GENERANDO CUADRADOS
# *******************


def gen_sq(n: int) -> list:
    """This function makes a list of all numbers squared in range of the parameter n.

    :param n: Defines the end limit for the range.
    :type n: int

    :return: A list containing all of the integers numbers squared given by the range.
    :rtype: list
    """
    return list(number**2 for number in range(n))
