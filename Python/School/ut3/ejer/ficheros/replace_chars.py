# ***********************
# REEMPLAZO DE CARACTERES
# ***********************
import filecmp
from pathlib import Path


def run(input_path: Path, replacements: str) -> bool:
    output_path = 'data/replace_chars/r_noticia.txt'
    f_input = open(input_path)
    with open(output_path, 'w') as f_output:
        splitted_replacements = replacements.split('|')
        for line in f_input:
            for old_char, new_char in splitted_replacements:
                line = line.replace(old_char, new_char)
            f_output.write(line)
    f_input.close()

    return filecmp.cmp(output_path, 'data/replace_chars/.expected', shallow=False)


if __name__ == '__main__':
    run('data/replace_chars/noticia.txt', 'áa|ée|íi|óo|úu')
