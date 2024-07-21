# **********************
# INICIALES DE UN NOMBRE
# **********************


def run(fullname: str) -> str:
    fullname = fullname.upper()

    fullname_list = [part.split(' ') for part in fullname.split(', ')]
    fullname_list.reverse()
    initials = ''
    if len(fullname_list[0]) > 1:
        del fullname_list[0][1]

    for name_part in fullname_list:
        for word in name_part:
            initials += f'{word[0]}.'

    return initials


if __name__ == '__main__':
    run('Delgado Quintero, sergio')
