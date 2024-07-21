# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path


def run(data_path: Path, target_word: str) -> list:
    f = open(data_path)
    matches = []
    line = 1
    SPECIAL_CHARS = '.,:;()\'¡!-'
    target = target_word.lower()

    for sentence in f:
        lowercase_sentence = sentence.lower().strip()
        for char in lowercase_sentence:
            if char in SPECIAL_CHARS:
                lowercase_sentence = lowercase_sentence.replace(char, ' ')
        if target in lowercase_sentence:
            word_index = 0
            target_number = lowercase_sentence.count(target)
            for _ in range(target_number):
                word_index = lowercase_sentence[word_index:].find(target) + 1 + word_index
                matches.append((line, word_index))
        line += 1
    f.close

    return matches


if __name__ == '__main__':
    run('data/find_words/bzrp.txt', 'persona')
