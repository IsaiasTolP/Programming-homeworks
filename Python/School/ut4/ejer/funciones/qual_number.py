# ********************
# CUALIFICANDO NÚMEROS
# ********************


def run(number: int) -> str:
    COMMA_POS = 3
    number = str(number)[::-1]
    counter = 0
    qnumber = ''
    for digit in number:
        if counter == COMMA_POS:
            counter = 0
            qnumber += f',{digit}'
        else:
            qnumber += digit
        counter += 1

    return qnumber[::-1]


if __name__ == '__main__':
    run(1)
