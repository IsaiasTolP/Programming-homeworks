# ******************
# LA PALABRA PERDIDA
# ******************


def run(text: str, target_word: str, replace_word: str) -> str:
    word_position = text.find(target_word)
    word_jump = len(target_word)
    text_start = text[:word_position]
    text_end = text[word_position + word_jump :]
    mtext = text_start + replace_word + text_end

    return mtext


if __name__ == '__main__':
    run('This is a beautiful night on the Atlantic', 'beautiful', 'terrible')
