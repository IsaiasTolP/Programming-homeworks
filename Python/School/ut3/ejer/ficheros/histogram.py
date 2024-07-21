# **********
# HISTOGRAMA
# **********
import filecmp
from pathlib import Path


def run(data_path: Path) -> bool:
    histogram_path = 'data/histogram/histogram.txt'
    f_input = open(data_path)
    chars = f_input.read().strip()
    BLOCK = '█'
    with open(histogram_path, 'w') as f_output:
        chars_freq = {char: chars.count(char) for char in sorted(chars)}
        for char, freq in chars_freq.items():
            num_blocks = BLOCK * freq
            f_output.write(f'{char} {num_blocks} {freq}\n')
    f_input.close()

    return filecmp.cmp(histogram_path, 'data/histogram/.expected', shallow=False)


if __name__ == '__main__':
    run('data/histogram/data.txt')
