VOWELS = 'aeiouáéíóúäëïöüàèìòù'

word = input('Introduzca una palabra curiosa (Ejemplo: Electroencefalografista): ').lower()
num_vowels = 0

for letter in word:
    if letter in VOWELS:
        num_vowels += 1

print(f'Su palabra tiene {num_vowels} vocales')
