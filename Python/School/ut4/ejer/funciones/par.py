def odd_splitter(numbers):
    evens = []
    odds = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)
    return evens, odds


values = [1, 2, 3, 4, 5, 6, 7, 8]
evens, odds = odd_splitter(values)
print(f'Los pares son {evens} y los impares {odds}')
