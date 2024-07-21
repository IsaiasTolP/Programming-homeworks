num_1 = 0
num_2 = 1

for _ in range(100):
    result = num_1 + num_2
    num_2 = num_1
    num_1 = result
    print(result, sep='\n')
