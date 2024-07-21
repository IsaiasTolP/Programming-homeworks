# **************
# HIPERFACTORIAL
# **************


def hyperfactorial(n: int) -> int:
    result = 1
    if n >= 1:
        for num in range(2, n + 1):
            result *= num**num
    return result
