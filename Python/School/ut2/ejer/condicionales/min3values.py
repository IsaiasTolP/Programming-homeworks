first_value = int(input('Ingrese un primer valor: '))
second_value = int(input('Ingrese un segundo valor: '))
third_value = int(input('Ingrese un tercer valor: '))

if first_value < second_value and first_value < third_value:
    print(first_value)
if second_value < first_value and second_value < third_value:
    print(second_value)
if third_value < first_value and third_value < second_value:
    print(third_value)
