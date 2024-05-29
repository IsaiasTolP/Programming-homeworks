# ****************
# NOMBRE VICEVERSA
# ****************


def run(fullname: str) -> str:
    name = fullname[: fullname.index(' ')]
    last_name = fullname[fullname.index(' ') + 1 :]
    swapname = f'{last_name} {name}'

    return swapname


if __name__ == '__main__':
    run('John McClane')
