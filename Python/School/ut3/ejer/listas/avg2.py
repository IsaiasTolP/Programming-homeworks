import sys

values = ','.join(sys.argv[1:])
int_values = [int(value) for value in values.split(',')]

num_values = len(int_values)
total = sum(int_values)
average = total / num_values
print(round(average, 2))
