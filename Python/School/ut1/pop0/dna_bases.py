# ********************
# EN LAS BASES DEL ADN
# ********************


def run(dna: str) -> tuple:
    PERCENT_COEF = 100
    dna_lenght = len(dna)

    adenines_rate = dna.count('A') / dna_lenght * PERCENT_COEF
    guanines_rate = dna.count('G') / dna_lenght * PERCENT_COEF
    thymines_rate = dna.count('T') / dna_lenght * PERCENT_COEF
    cytosines_rate = dna.count('C') / dna_lenght * PERCENT_COEF

    return adenines_rate, guanines_rate, thymines_rate, cytosines_rate


if __name__ == '__main__':
    run('GGTTACCAACCCAGTCGAAAATTTGGTCAGGG')
