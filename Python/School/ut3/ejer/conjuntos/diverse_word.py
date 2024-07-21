# ***************
# PALABRA DIVERSA
# ***************


def run(words: list) -> str:
    max_letters = 0
    for word in words:
        diff_letters = len(set(word))
        if diff_letters >= max_letters:
            dword, max_letters = word, diff_letters

    return dword


if __name__ == '__main__':
    run(['dictionary', 'turtle', 'flexibility', 'humanity'])
