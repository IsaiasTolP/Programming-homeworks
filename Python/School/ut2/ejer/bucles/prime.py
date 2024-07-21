number = int(input('Introduzca un número entero cualquiera: '))
range_end = number + 1
div_points = 0

for value in range(1, range_end):
    if number % value == 0:
        div_points += 1

if div_points == 2 or number == 1:
    print('Su número es primo')
else:
    print('Su número no es primo')
