# *******************
# CONTANDO SIN CONTAR
# *******************


def mcount(items: tuple = (), target: int = 0) -> int:
    """Calculate the number of times target values show in a tuple containing items:

    :param items: represents a tuple containing a X number of items, defaults to ().
    :type items: tuple
    :param target: represents a specific item the function is looking for to count, defaults to 0.
    :type target: int

    :return: the function returns a value representing how many times the target item showed up.
    :rtype: int
    """
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count
