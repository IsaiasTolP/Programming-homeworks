# ******************
# DESCOMPONIENDO RGB
# ******************


def run(rgb_color: str) -> tuple:
    clean_colors = rgb_color.strip('()')
    colors_alternative_sep = clean_colors.replace(',', '-', 1)

    hyphen_index = colors_alternative_sep.index('-')
    comma_index = colors_alternative_sep.index(',')

    red = int(clean_colors[:hyphen_index])
    green = int(clean_colors[hyphen_index + 1 : comma_index])
    blue = int(clean_colors[comma_index + 1 :])

    return red, green, blue


if __name__ == '__main__':
    run('(161,49,247)')
