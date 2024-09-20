# ************************
# CONVERSOR DE TEMPERATURA
# ************************


def temp_converter(source: str):
    def temp_changer(temp: float):
        if source == 'c2f':
            result = round(temp * 1.8 + 32, 2)
        elif source == 'f2c':
            result = round((temp - 32) / 1.8, 2)
        else:
            return None
        return result

    return temp_changer


def run(source: str, temp: float) -> float:
    converter = temp_converter(source)
    result = converter(temp)
    return result
