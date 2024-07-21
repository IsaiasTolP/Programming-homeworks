max_number = int(input("Introduzca el número máximo al que quiere llegar: "))
num = 0

while num < max_number:
    num += 5
    if num < max_number:
        print(num)
