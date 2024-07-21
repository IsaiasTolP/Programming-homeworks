# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************


def to_string(freqs):
    formated_freqs = ''
    for freq in freqs:
        current_string = f'{freq[0]}:{freq[1]},'
        formated_freqs += current_string
    return formated_freqs.rstrip(',')


def cfreq(items, /, as_string=False):
    freqs = []

    if items:
        freq = 0
        current_item = items[0]
        for item in items:
            if item == current_item:
                freq += 1
            else:
                freqs.append((current_item, freq))
                freq = 1
                current_item = item
        freqs.append((current_item, freq))

    if as_string:
        freqs = to_string(freqs)
    return freqs
