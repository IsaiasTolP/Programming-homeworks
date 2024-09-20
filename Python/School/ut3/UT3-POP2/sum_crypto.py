# ******************
# SUMA CRIPTOGRÁFICA
# ******************
from pathlib import Path


def run(crypto_path: Path) -> float:
    sum_cr = 0
    CRYPTO_CODES = {
        'sd': '-',
        'vo': '.',
        'ax': '0',
        'gh': '1',
        'hj': '2',
        'uv': '3',
        'ws': '4',
        'pk': '5',
        'et': '6',
        'mc': '7',
        'rh': '8',
        'wb': '9',
    }
    f = open(crypto_path)
    for line in f:
        unencrypted_num = ''
        for index in range(0, len(line.strip()), 2):
            code = line[index : index + 2]
            if code in CRYPTO_CODES:
                unencrypted_num += CRYPTO_CODES[code]
        sum_cr += float(unencrypted_num)

    sum_cr = round(sum_cr, 3)
    f.close()

    return sum_cr


if __name__ == '__main__':
    run('data/sum_crypto/data1.crypto')
