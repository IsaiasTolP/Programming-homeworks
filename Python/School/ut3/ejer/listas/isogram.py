# *********************
# ENCONTRANDO ISOGRAMAS
# *********************


def run(text: str) -> bool:
    ALPHABET = "abcdefghijklmnñopqrstuvwxyz"
    text = text.lower()
    appeared_letter_list = []

    is_isogram = True

    for char in text:
        if char in ALPHABET:
            if char not in appeared_letter_list:
                appeared_letter_list.append(char)
            else:
                is_isogram = False
                break

    return is_isogram


if __name__ == '__main__':
    run('lumberjacks')
