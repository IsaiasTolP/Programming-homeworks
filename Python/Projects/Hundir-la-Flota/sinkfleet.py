import random
import string

EMPTY = ''

UNEXPLORED = '⬛'
WATER = '🟦'
TOUCHED = '🟧'
SUNKEN = '🟥'


def generate_board(
    size: int = 10,
    sheeps: tuple[tuple[int, int]] = ((5, 1), (4, 1), (3, 2), (2, 1)),
) -> list[list[str]]:
    board = [[EMPTY for _ in range(size)] for _ in range(size)]
    for sheep_size, num_sheeps in sheeps:
        placed_sheeps = 0
        while placed_sheeps < num_sheeps:
            sheep_id = f'{sheep_size}{string.ascii_uppercase[placed_sheeps]}'
            row, col = random.randint(0, size), random.randint(0, size)
            step = random.choice((-1, 1))
            row_step, col_step = (step, 0) if random.randint(0, 1) else (0, step)
            breadcrumbs = []
            for _ in range(sheep_size):
                try:
                    if not (0 <= row < size and 0 <= col < size):
                        raise IndexError()
                    if board[row][col] == EMPTY:
                        board[row][col] = sheep_id
                        breadcrumbs.append((row, col))
                    else:
                        raise IndexError()
                    row += row_step
                    col += col_step
                except IndexError:
                    # reset board
                    for bc in breadcrumbs:
                        board[bc[0]][bc[1]] = EMPTY
                    break
            else:
                placed_sheeps += 1

    return board


def show_board(board: list[list[str]]) -> None:
    for row in board:
        for item in row:
            print(f'[{item:2s}]', end='')
        print()


# TU CÓDIGO DESDE AQUÍ HACIA ABAJO
# ↓↓↓↓↓↓↓↓↓


board = generate_board()

ships = []
for row in board:
    for box in row:
        if box and box not in ships:
            ships.append(box)
to_hit = [ship for ship in ships for _ in range(int(ship[0]))]

print('Bienvenido al juego de hundir la flota')
player_name = input('Introduzca su nombre de jugador: ')
gender_options = ['m', 'f']
gender = (input('Elija su género(M/F): ').lower())
print()

if gender not in gender_options:
    gender = 'm'

if gender == 'm':
    title = 'Capitán'
else:
    title = 'Capitana'

COLUNMS = [n for n in range(1, 11)]
ROWS = 'ABCDEFGHIJ'
points = 0

# Código de impresión de tablero
print('Este será el tablero en el que jugaremos')
print()

print('   ', end='')
for col_num in COLUNMS:
    print(col_num, end='  ')
print()

for row_index, row in enumerate(board):
    print(ROWS[row_index], end=' ')
    for col in row:
        print(UNEXPLORED, end=' ')
    print()
print()

# codigo de los intentos
while to_hit:
    target = (input(f'Ingrese la posición de disparo {title} {player_name}: ').upper())
    print()

    c_limit = False
    count_char = 0
    for char in target:
        if char.isalpha():
            count_char += 1
        if count_char > 1:
            c_limit = True
            break
    if c_limit:
        print('Su coordenada no es válida')
        continue

    if target[0].isnumeric():
        row_target = ROWS.find(target[-1])
        col_target = int(target[:-1]) - 1
    else:
        target = target[1:] + target[0]
        row_target = ROWS.find(target[-1])
        col_target = int(target[:-1]) - 1

    if row_target == -1 or row_target < 0 or row_target > 9:
        print('Su coordenada no es válida')
        continue

    target = board[row_target][col_target]

    # Código que compruebe que a la casilla no se la haya disparado

    if isinstance(target, tuple):
        print('¡YA HEMOS DISPARADO A ESA POSICIÓN!, había un barco ¿Recuerda?.')
        continue
    elif target == 'water':
        print('¡YA HEMOS DISPARADO A ESA POSICIÓN!, no había nada ¿Recuerda?.')
        continue
    elif isinstance(target, int):
        print('¡YA HEMOS DISPARADO A ESA POSICIÓN, El barco que había ya está destruido!')
        continue

    # Este es el código que detecta si hay agua o un barco (Hay que añadir la puntuación)

    if target:
        to_hit.remove(target)
        ship_lenght = int(target[0])
        board[row_target][col_target] = (ship_lenght, target[1])
        if target in to_hit:
            points += 2 * ship_lenght
            hit_type = 'Tocado'
        else:
            for row_index, row in enumerate(board):
                for box_index, box in enumerate(row):
                    if box == (ship_lenght, target[1]):
                        board[row_index][box_index] = ship_lenght
            points += 4 * ship_lenght
            hit_type = 'Tocado y Hundido'
    else:
        board[row_target][col_target] = 'water'
        hit_type = 'Agua'
        if points != 0:
            points -= 1

    # Se imprime el tablero al final del turno
    print('   ', end='')
    for col_num in COLUNMS:
        print(col_num, end='  ')
    print()
    for row_index, row in enumerate(board):
        print(ROWS[row_index], end=' ')
        for col_index, col in enumerate(row):
            coordinate = board[row_index][col_index]
            if isinstance(coordinate, tuple):
                print(TOUCHED, end=' ')
            elif isinstance(coordinate, int):
                print(SUNKEN, end=' ')
            elif coordinate == 'water':
                print(WATER, end=' ')
            else:
                print(UNEXPLORED, end=' ')
        print()

    print(hit_type)
    print(f'Tu puntuación es de {points}')
    print()

# Cuando se sale del bucle se imprimen los mensajes de fin juego
print(f'¡Has destruido todos los barcos {player_name}!')
print('Veamos tu puntacion...')
print(f'¡Tu puntuación es de {points}! ¡¡¡HAS GANADO!!!')
