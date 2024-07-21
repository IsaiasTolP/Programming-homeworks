# *************************
# SIMULANDO EL COMANDO TAIL
# *************************
from pathlib import Path


def run(file: Path, n: int) -> str:
    f = open(file)
    all_lines = f.readlines()
    lines = ''.join(all_lines[-n:]).strip()
    f.close()

    return lines


if __name__ == '__main__':
    run('data/head/nba_season22.txt', 3)
