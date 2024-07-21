STR_ONE = '1'

repeat_num = 1
multiplication_limit = 10

for _ in range(multiplication_limit):
    multi_coef = int(STR_ONE * repeat_num)
    result = multi_coef * multi_coef
    print(result)
    repeat_num += 1
