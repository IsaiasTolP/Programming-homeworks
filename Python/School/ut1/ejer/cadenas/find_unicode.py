# ********************
# ENCUENTRE EL UNICODE
# ********************


def run(source_char: str, offset: int) -> str:
    modified_source_char = ord(source_char) + offset
    target_char = chr(modified_source_char)

    return target_char


if __name__ == '__main__':
    run('δ', -2)
