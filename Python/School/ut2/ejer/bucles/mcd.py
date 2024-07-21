num_a = int(input('Introduzca su primer número: '))
num_b = int(input('Introduzca su segundo número: '))

if num_a > num_b:
    for divisor in range(1, num_b + 1):
        if num_a % divisor == 0 and num_b % divisor == 0:
            common_divisor = divisor
else:
    for divisor in range(1, num_a + 1):
        if num_a % divisor == 0 and num_b % divisor == 0:
            common_divisor = divisor

print(common_divisor)
