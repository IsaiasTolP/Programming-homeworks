domino_right_start = 0
domino_left_start = 0
domino_range_end = 7

for domino_left_num in range(domino_right_start, domino_range_end):
    for domino_right_num in range(domino_left_start, domino_range_end):
        print(domino_left_num, domino_right_num, sep='|')
    domino_left_start += 1
