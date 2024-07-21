def to_sum(values):
    if isinstance(values, list):
        result = 0
        for value in values:
            result += value
            print(f'El resultado es {result}')
    else:
        exit


values = []
while True:
    value = float(input('Introduzca un valor: '))
    values.append(value)
    if to_continue := input('¿Quiere introducir otro valor?(S/N): ').lower() != 's':
        break

to_sum(values)
