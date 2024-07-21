LETTER_X = 'X'
LETTER_U = 'U'
LETTER_D = 'D'
GAP = ' '

lines_and_column_num = int(input('¿Cuántas columnas y filas quiere?: '))

x_position = 1

for column in range(lines_and_column_num):
    u_number = lines_and_column_num - x_position
    d_number = x_position - 1
    d_line = (LETTER_D + GAP) * d_number
    u_line = (LETTER_U + GAP) * u_number
    print(d_line, LETTER_X + GAP, u_line, sep='')
    x_position += 1
