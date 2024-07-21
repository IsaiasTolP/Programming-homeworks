def carambola(a, b):
    if isinstance(a, list):
        result = 0
        for number in a:
            result += number
        return result
    if b is not None:
        return a + b


carambola
turu = 1
tara = 2

print(carambola(turu, tara))
