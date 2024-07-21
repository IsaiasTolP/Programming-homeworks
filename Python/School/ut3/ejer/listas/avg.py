import sys

values = [int(i) for i in sys.argv[1:]]

num_values = len(values)
total = sum(values)
average = total / num_values
print(round(average, 2))
